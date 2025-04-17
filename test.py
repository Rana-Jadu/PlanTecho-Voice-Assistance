from flask import Flask, request, jsonify
import os
import speech_recognition as sr
from gtts import gTTS
import tempfile
import base64
from langdetect import detect
import google.generativeai as genai

app = Flask(__name__, static_folder='.', static_url_path='')

# Configure Gemini API
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def process_audio(audio_data):
    """Process audio data from web and return text"""
    recognizer = sr.Recognizer()
    
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
        tmp.write(audio_data)
        tmp_path = tmp.name
    
    try:
        with sr.AudioFile(tmp_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio, language="ar-EG")
                return text
            except:
                text = recognizer.recognize_google(audio, language="en-US")
                return text
    except Exception as e:
        return None
    finally:
        os.unlink(tmp_path)

def generate_response(text):
    """Generate plant expert response with better error handling"""
    if not text:
        return {
            'text': "لا يمكنني الحصول على المعلومات الآن",
            'error': True
        }
    
    try:
        lang = detect(text)
    except:
        lang = "ar"  # Default to Arabic if detection fails
    
    try:
        prompt = (
            "You are a plant expert. Answer concisely in the same language as the question. "
            "If not plant-related, say: 'أسئلة النباتات فقط' in Arabic or "
            "'Plant questions only' in English.\n\n"
            f"Question: {text}"
        )
        
        response = model.generate_content(prompt)
        
        if not response or not hasattr(response, 'text'):
            return {
                'text': "حدث خطأ في النظام. يرجى المحاولة لاحقاً",  # "System error, please try later"
                'error': True
            }
            
        return {
            'text': response.text,
            'error': False
        }
        
    except Exception as e:
        print(f"Gemini Error: {str(e)}")
        return {
            'text': "خدمة الخبراء غير متوفرة حالياً",  # "Expert service unavailable"
            'error': True
        }

def text_to_speech(text):
    """Convert text to speech using gTTS and return as base64"""
    if not text:
        return None

    try:
        lang = detect(text)
    except:
        lang = "en"
    
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='ar' if lang == 'ar' else 'en')
    
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
        tmp_path = tmp.name
        tts.save(tmp_path)
    
    # Read the audio file and convert to base64
    with open(tmp_path, 'rb') as f:
        audio_data = f.read()
    
    os.unlink(tmp_path)
    return base64.b64encode(audio_data).decode('utf-8')

@app.route('/')
def serve_html():
    return app.send_static_file('test2.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    audio_data = None
    
    if data.get('audio'):
        audio_data = base64.b64decode(data['audio'])
        user_message = process_audio(audio_data)
    
    bot_response = generate_response(user_message)
    audio_response = text_to_speech(bot_response['text'])
    
    return jsonify({
        'response': bot_response,
        'audio': f"data:audio/mp3;base64,{audio_response}" if audio_response else None
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
