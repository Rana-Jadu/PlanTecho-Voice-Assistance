# # # # import pyttsx3

# # # # engine = pyttsx3.init()
# # # # voices = engine.getProperty('voices')

# # # # for voice in voices:
# # # #     print(f"ID: {voice.id}, Name: {voice.name}, Language: {voice.languages}")

# # # # # تجربة الصوت العربي
# # # # arabic_voice = None
# # # # for voice in voices:
# # # #     if "Arabic" in voice.name or "ar" in voice.id:
# # # #         arabic_voice = voice.id
# # # #         break

# # # # if arabic_voice:
# # # #     engine.setProperty("voice", arabic_voice)
# # # #     engine.say("مرحبا، هذا اختبار للصوت العربي")
# # # #     engine.runAndWait()
# # # # else:
# # # #     print("❌ لا يوجد صوت عربي متاح. تأكد من تثبيته في إعدادات النظام.")


# # # # import speech_recognition as sr

# # # # def recognize_arabic_speech():
# # # #     # Initialize recognizer
# # # #     r = sr.Recognizer()
    
# # # #     # Use microphone as source
# # # #     with sr.Microphone() as source:
# # # #         print("Speak in Arabic now (Egyptian dialect)...")
        
# # # #         # Adjust for ambient noise (better accuracy)
# # # #         r.adjust_for_ambient_noise(source, duration=1)
        
# # # #         # Listen for audio input
# # # #         audio = r.listen(source, timeout=5, phrase_time_limit=10)
    
# # # #     try:
# # # #         # Recognize using Google Speech Recognition (Arabic - Egypt)
# # # #         text = r.recognize_google(audio, language="ar-EG")
# # # #         print("You said (Arabic):", text)
# # # #         return text
        
# # # #     except sr.UnknownValueError:
# # # #         print("Google Speech Recognition could not understand audio")
# # # #     except sr.RequestError as e:
# # # #         print(f"Could not request results from Google; {e}")
# # # #     except Exception as e:
# # # #         print(f"Error: {e}")

# # # # # Call the function
# # # # recognize_arabic_speech()





# # # # import speech_recognition as sr
# # # # import pyttsx3

# # # # def setup_tts():
# # # #     engine = pyttsx3.init()
# # # #     # Configure voice (try to find Arabic voice)
# # # #     voices = engine.getProperty('voices')
# # # #     arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
# # # #     if arabic_voices:
# # # #         engine.setProperty('voice', arabic_voices[0].id)
# # # #     return engine

# # # # def recognize_and_respond():
# # # #     recognizer = sr.Recognizer()
# # # #     tts_engine = setup_tts()
    
# # # #     with sr.Microphone() as source:
# # # #         # Initial prompt
# # # #         tts_engine.say("تحدث باللغة العربية الآن")  # "Speak in Arabic now"
# # # #         tts_engine.runAndWait()
# # # #         print("Listening... (Arabic)")
        
# # # #         recognizer.adjust_for_ambient_noise(source)
# # # #         audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    
# # # #     try:
# # # #         # Recognize Arabic speech
# # # #         text = recognizer.recognize_google(audio, language="ar-EG")
# # # #         print("You said:", text)
        
# # # #         # Create response
# # # #         response = f"لقد قلت: {text}"  # "You said: {text}"
        
# # # #         # Speak the response
# # # #         tts_engine.say(response)
# # # #         tts_engine.runAndWait()
        
# # # #         return text
        
# # # #     except sr.UnknownValueError:
# # # #         error_msg = "لم أستطع فهم ما قلته"  # "I couldn't understand what you said"
# # # #         tts_engine.say(error_msg)
# # # #         tts_engine.runAndWait()
# # # #         print(error_msg)
# # # #     except sr.RequestError:
# # # #         error_msg = "حدث خطأ في الاتصال بالخدمة"  # "Service connection error"
# # # #         tts_engine.say(error_msg)
# # # #         tts_engine.runAndWait()
# # # #         print(error_msg)

# # # # # Run the program
# # # # while True:
# # # #     recognize_and_respond()
# # # #     if input("Press 'q' to quit, any other key to continue: ").lower() == 'q':
# # # #         break





# # # import speech_recognition as sr
# # # import pyttsx3
# # # import threading
# # # import queue
# # # import time

# # # class ArabicVoiceAssistant:
# # #     def __init__(self):
# # #         self.recognizer = sr.Recognizer()
# # #         self.tts_engine = self.setup_tts()
# # #         self.audio_queue = queue.Queue()
# # #         self.is_listening = False

# # #     def setup_tts(self):
# # #         engine = pyttsx3.init()
# # #         # Configure Arabic voice (if available)
# # #         voices = engine.getProperty('voices')
# # #         for voice in voices:
# # #             if 'arabic' in voice.name.lower() or 'ar-' in voice.id.lower():
# # #                 engine.setProperty('voice', voice.id)
# # #                 break
# # #         return engine

# # #     def speak(self, text):
# # #         """Speak text immediately"""
# # #         print(f"Assistant: {text}")
# # #         self.tts_engine.say(text)
# # #         self.tts_engine.runAndWait()

# # #     def listen_loop(self):
# # #         """Continuous listening with audio feedback"""
# # #         self.speak("مرحباً، أنا جاهز للاستماع إليك")
        
# # #         while self.is_listening:
# # #             try:
# # #                 with sr.Microphone() as source:
# # #                     self.recognizer.adjust_for_ambient_noise(source)
# # #                     self.speak("تحدث الآن")
                    
# # #                     try:
# # #                         audio = self.recognizer.listen(
# # #                             source, 
# # #                             timeout=3, 
# # #                             phrase_time_limit=5
# # #                         )
# # #                         self.process_audio(audio)
                        
# # #                     except sr.WaitTimeoutError:
# # #                         self.speak("لم أسمع أي شيء، حاول مرة أخرى")
                        
# # #             except Exception as e:
# # #                 self.speak(f"حدث خطأ: {str(e)}")
# # #                 time.sleep(1)

# # #     def process_audio(self, audio):
# # #         """Process audio with loading feedback"""
# # #         self.speak("جارٍ المعالجة...")
        
# # #         try:
# # #             # Recognize in a separate thread to prevent freezing
# # #             def recognition_thread():
# # #                 try:
# # #                     text = self.recognizer.recognize_google(audio, language="ar-EG")
# # #                     self.audio_queue.put(f"لقد سمعتك تقول: {text}")
# # #                 except Exception as e:
# # #                     self.audio_queue.put(f"خطأ في التعرف: {str(e)}")

# # #             thread = threading.Thread(target=recognition_thread)
# # #             thread.start()
            
# # #             # Give feedback while processing
# # #             while thread.is_alive():
# # #                 self.tts_engine.say("...")
# # #                 self.tts_engine.runAndWait()
# # #                 time.sleep(1)
            
# # #             # Get the result
# # #             response = self.audio_queue.get()
# # #             self.speak(response)
            
# # #         except Exception as e:
# # #             self.speak(f"حدث خطأ أثناء المعالجة: {str(e)}")

# # #     def start(self):
# # #         """Start the assistant"""
# # #         self.is_listening = True
# # #         listen_thread = threading.Thread(target=self.listen_loop)
# # #         listen_thread.start()
        
# # #         try:
# # #             while self.is_listening:
# # #                 time.sleep(0.1)
# # #         except KeyboardInterrupt:
# # #             self.is_listening = False
# # #             self.speak("مع السلامة")
# # #             listen_thread.join()

# # # # Run the assistant
# # # if __name__ == "__main__":
# # #     assistant = ArabicVoiceAssistant()
# # #     print("Starting Arabic Voice Assistant...")
# # #     assistant.start()



# # import os
# # import speech_recognition as sr
# # import pyttsx3
# # from langdetect import detect
# # import google.generativeai as genai
# # import threading

# # # Load API Key from environment variables
# # GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
# # if not GENAI_API_KEY:
# #     raise ValueError("Missing API key. Set GEMINI_API_KEY as an environment variable.")

# # # Configure Gemini API
# # genai.configure(api_key=GENAI_API_KEY)
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Initialize Text-to-Speech engine with Arabic support
# # def setup_tts():
# #     engine = pyttsx3.init()
# #     # Try to find Arabic voice
# #     voices = engine.getProperty('voices')
# #     arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
# #     if arabic_voices:
# #         engine.setProperty('voice', arabic_voices[0].id)
# #     return engine

# # tts_engine = setup_tts()

# # # Enhanced Speech Recognition Function with Arabic prompts
# # def recognize_speech():
# #     """Recognizes speech input from the user in Arabic or English."""
# #     recognizer = sr.Recognizer()
    
# #     with sr.Microphone() as source:
# #         # Speak Arabic prompt
# #         tts_engine.say("تحدث الآن، أنا أستمع إليك")  # "Speak now, I'm listening to you"
# #         tts_engine.runAndWait()
# #         print("Listening... (Arabic/English)")
        
# #         recognizer.adjust_for_ambient_noise(source)
        
# #         try:
# #             audio = recognizer.listen(source, timeout=5)
# #             try:
# #                 # First try Arabic recognition
# #                 text = recognizer.recognize_google(audio, language="ar-EG")
# #                 print(f"You said (Arabic): {text}")
# #                 return text
# #             except:
# #                 # Fallback to English if Arabic fails
# #                 text = recognizer.recognize_google(audio, language="en-US")
# #                 print(f"You said (English): {text}")
# #                 return text
        
# #         except sr.UnknownValueError:
# #             error_msg = "لم أستطع فهم ما قلته"  # "I couldn't understand what you said"
# #             tts_engine.say(error_msg)
# #             tts_engine.runAndWait()
# #             return None
# #         except sr.RequestError:
# #             error_msg = "حدث خطأ في الاتصال بالخدمة"  # "Service connection error"
# #             tts_engine.say(error_msg)
# #             tts_engine.runAndWait()
# #             return None
# #         except sr.WaitTimeoutError:
# #             error_msg = "انتهى وقت الانتظار"  # "Timeout occurred"
# #             tts_engine.say(error_msg)
# #             tts_engine.runAndWait()
# #             return None

# # # Language Detection Function
# # def detect_language(text):
# #     """Detects the language of the user's input."""
# #     try:
# #         return detect(text)
# #     except:
# #         return "unknown"

# # # Generating Response Function with Arabic support
# # def ask_gemini(user_input):
# #     """Ensures Gemini responds ONLY to plant-related questions in the detected language."""
    
# #     # Detect language of the input
# #     lang = detect_language(user_input)

# #     # Define the prompt for Gemini AI
# #     prompt = (
# #         "You are a plant expert. Answer ONLY plant-related questions. "
# #         "Respond in the same language as the question. "
# #         "If the question is about plants, provide a detailed response. "
# #         "If not, reply with: 'I only answer plant-related questions.'\n\n"
# #         f"User question: {user_input}"
# #     )

# #     try:
# #         response = model.generate_content(prompt)
        
# #         if not response or not hasattr(response, 'text'):
# #             error_msg = "لا يمكنني الحصول على المعلومات الآن"  # "Can't get information now"
# #             tts_engine.say(error_msg)
# #             tts_engine.runAndWait()
# #             return error_msg
        
# #         response_text = response.text
        
# #         # Speak loading message while processing
# #         tts_engine.say("جارٍ المعالجة" if lang == "ar" else "Processing")
# #         tts_engine.runAndWait()
        
# #         # Speak the response
# #         speak_response(response_text, lang)
# #         return response_text
    
# #     except Exception as e:
# #         error_msg = f"حدث خطأ: {str(e)}" if lang == "ar" else f"Error: {str(e)}"
# #         tts_engine.say(error_msg)
# #         tts_engine.runAndWait()
# #         return error_msg
    
# # # Enhanced Reading Response Function
# # def speak_response(text, lang):
# #     """Converts text to speech based on detected language."""
# #     # Set appropriate voice if available
# #     voices = tts_engine.getProperty('voices')
# #     if lang == "ar":
# #         arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
# #         if arabic_voices:
# #             tts_engine.setProperty('voice', arabic_voices[0].id)
    
# #     tts_engine.say(text)
# #     tts_engine.runAndWait()

# # if __name__ == "__main__":
# #     while True:
# #         user_question = recognize_speech()
# #         if user_question:
# #             bot_response = ask_gemini(user_question)
# #             print(f"\nGemini Response: {bot_response}")
        
# #         # Continue or quit
# #         tts_engine.say("اضغط زر الإدخال للمتابعة أو اكتب خروج للإنهاء")
# #         tts_engine.runAndWait()
# #         user_input = input("\nPress Enter to continue or type 'exit' to quit: ")
# #         if user_input.lower() == 'exit':
# #             tts_engine.say("مع السلامة")  # "Goodbye"
# #             tts_engine.runAndWait()
# #             break



# import os
# import speech_recognition as sr
# import pyttsx3
# from langdetect import detect
# import google.generativeai as genai
# import threading

# # Load API Key from environment variables
# GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GENAI_API_KEY:
#     raise ValueError("Missing API key. Set GEMINI_API_KEY as an environment variable.")

# # Configure Gemini API
# genai.configure(api_key=GENAI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# # Initialize Text-to-Speech engine with Arabic support
# def setup_tts():
#     engine = pyttsx3.init()
#     # Try to find Arabic voice
#     voices = engine.getProperty('voices')
#     arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
#     if arabic_voices:
#         engine.setProperty('voice', arabic_voices[0].id)
#     return engine

# tts_engine = setup_tts()

# # Enhanced Speech Recognition Function with unlimited listening time
# def recognize_speech():
#     """Recognizes speech input from the user in Arabic or English without time constraints."""
#     recognizer = sr.Recognizer()
    
#     with sr.Microphone() as source:
#         # Speak Arabic prompt
#         tts_engine.say("تحدث الآن، أنا أستمع إليك")  # "Speak now, I'm listening to you"
#         tts_engine.runAndWait()
#         print("Listening... (Arabic/English)")
        
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         recognizer.dynamic_energy_threshold = True
#         recognizer.pause_threshold = 1.5  # Wait longer for speech to end
        
#         try:
#             # Remove timeout parameter for unlimited listening
#             audio = recognizer.listen(source)
#             try:
#                 # First try Arabic recognition
#                 text = recognizer.recognize_google(audio, language="ar-EG")
#                 print(f"You said (Arabic): {text}")
#                 return text
#             except:
#                 # Fallback to English if Arabic fails
#                 text = recognizer.recognize_google(audio, language="en-US")
#                 print(f"You said (English): {text}")
#                 return text
        
#         except sr.UnknownValueError:
#             error_msg = "لم أستطع فهم ما قلته"  # "I couldn't understand what you said"
#             tts_engine.say(error_msg)
#             tts_engine.runAndWait()
#             return None
#         except sr.RequestError:
#             error_msg = "حدث خطأ في الاتصال بالخدمة"  # "Service connection error"
#             tts_engine.say(error_msg)
#             tts_engine.runAndWait()
#             return None

# # Language Detection Function
# def detect_language(text):
#     """Detects the language of the user's input."""
#     try:
#         return detect(text)
#     except:
#         return "unknown"

# # Generating Response Function with Arabic support
# def ask_gemini(user_input):
#     """Ensures Gemini responds ONLY to plant-related questions in the detected language."""
    
#     # Detect language of the input
#     lang = detect_language(user_input)

#     # Define the prompt for Gemini AI
#     prompt = (
#         "You are a plant expert. Answer ONLY plant-related questions. "
#         "Respond in the same language as the question. "
#         "If the question is about plants, provide a detailed response. "
#         "If not, reply with: 'I only answer plant-related questions.'\n\n"
#         f"User question: {user_input}"
#     )

#     try:
#         # Speak processing message in the detected language
#         processing_msg = "جارٍ المعالجة" if lang == "ar" else "Processing"
#         tts_engine.say(processing_msg)
#         tts_engine.runAndWait()
        
#         response = model.generate_content(prompt)
        
#         if not response or not hasattr(response, 'text'):
#             error_msg = "لا يمكنني الحصول على المعلومات الآن"  # "Can't get information now"
#             tts_engine.say(error_msg)
#             tts_engine.runAndWait()
#             return error_msg
        
#         response_text = response.text
        
#         # Speak the response
#         speak_response(response_text, lang)
#         return response_text
    
#     except Exception as e:
#         error_msg = f"حدث خطأ: {str(e)}" if lang == "ar" else f"Error: {str(e)}"
#         tts_engine.say(error_msg)
#         tts_engine.runAndWait()
#         return error_msg
    
# # Enhanced Reading Response Function
# def speak_response(text, lang):
#     """Converts text to speech based on detected language."""
#     # Set appropriate voice if available
#     voices = tts_engine.getProperty('voices')
#     if lang == "ar":
#         arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
#         if arabic_voices:
#             tts_engine.setProperty('voice', arabic_voices[0].id)
    
#     # Split long responses into chunks to prevent buffer overflow
#     max_chars = 200  # Adjust based on your TTS engine's limits
#     chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
    
#     for chunk in chunks:
#         tts_engine.say(chunk)
#         tts_engine.runAndWait()

# if __name__ == "__main__":
#     while True:
#         user_question = recognize_speech()
#         if user_question:
#             bot_response = ask_gemini(user_question)
#             print(f"\nGemini Response: {bot_response}")
        
#         # Continue or quit
#         tts_engine.say("اضغط زر الإدخال للمتابعة أو اكتب خروج للإنهاء")
#         tts_engine.runAndWait()
#         user_input = input("\nPress Enter to continue or type 'exit' to quit: ")
#         if user_input.lower() == 'exit':
#             tts_engine.say("مع السلامة")  # "Goodbye"
#             tts_engine.runAndWait()
#             break



######################## ده الكود النهائي #########################اللي شغالة عليه
from flask import Flask, request, jsonify
import os
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from langdetect import detect
import google.generativeai as genai
import tempfile
import base64

app = Flask(__name__, static_folder='.', static_url_path='')   ### اظبطيها 

# Configure Gemini API
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize TTS engine
def setup_tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
    if arabic_voices:
        engine.setProperty('voice', arabic_voices[0].id)
    return engine

tts_engine = setup_tts()

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
    """Convert text to speech and return as base64"""
    if not text:
        return None
        
    try:
        lang = detect(text)
    except:
        lang = "en"
    
    if lang == "ar":
        arabic_voices = [v for v in tts_engine.getProperty('voices') 
                        if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
        if arabic_voices:
            tts_engine.setProperty('voice', arabic_voices[0].id)
    
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
        tmp_path = tmp.name
    
    tts_engine.save_to_file(text, tmp_path)
    tts_engine.runAndWait()
    
    with open(tmp_path, 'rb') as f:
        audio_data = f.read()
    
    os.unlink(tmp_path)
    return base64.b64encode(audio_data).decode('utf-8')

@app.route('/')
def serve_html():
    return app.send_static_file('voice_assis.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    audio_data = None
    
    if data.get('audio'):
        audio_data = base64.b64decode(data['audio'])
        user_message = process_audio(audio_data)
    
    bot_response = generate_response(user_message)
    audio_response = text_to_speech(bot_response)
    
    return jsonify({
        'response': bot_response,
        'audio': f"data:audio/mp3;base64,{audio_response}" if audio_response else None
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
























# from flask import Flask, request, jsonify
# import os
# import speech_recognition as sr
# from gtts import gTTS
# import tempfile
# import base64
# from langdetect import detect
# import google.generativeai as genai

# app = Flask(__name__, static_folder='.', static_url_path='')

# # Configure Gemini API
# GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GENAI_API_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro")

# def process_audio(audio_data):
#     """Process audio data from web and return text with improved language detection"""
#     recognizer = sr.Recognizer()
    
#     with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
#         tmp.write(audio_data)
#         tmp_path = tmp.name
    
#     try:
#         with sr.AudioFile(tmp_path) as source:
#             audio = recognizer.record(source)
#             try:
#                 text = recognizer.recognize_google(audio, language="ar-EG")
#                 return {'text': text, 'lang': 'ar'}
#             except:
#                 text = recognizer.recognize_google(audio, language="en-US")
#                 return {'text': text, 'lang': 'en'}
#     except Exception as e:
#         print(f"Audio processing error: {str(e)}")
#         return None
#     finally:
#         os.unlink(tmp_path)

# def generate_response(text):
#     """Generate plant expert response with better error handling"""
#     if not text:
#         return {
#             'text': "لا يمكنني الحصول على المعلومات الآن",
#             'error': True
#         }
    
#     try:
#         lang = detect(text)
#     except:
#         lang = "ar"  # Default to Arabic if detection fails
    
#     try:
#         prompt = (
#             "You are a plant expert. Answer concisely in the same language as the question. "
#             "If not plant-related, say: 'أسئلة النباتات فقط' in Arabic or "
#             "'Plant questions only' in English.\n\n"
#             f"Question: {text}"
#         )
        
#         response = model.generate_content(prompt)
        
#         if not response or not hasattr(response, 'text'):
#             return {
#                 'text': "حدث خطأ في النظام. يرجى المحاولة لاحقاً",  # "System error, please try later"
#                 'error': True
#             }
            
#         return {
#             'text': response.text,
#             'error': False
#         }
        
#     except Exception as e:
#         print(f"Gemini Error: {str(e)}")
#         return {
#             'text': "خدمة الخبراء غير متوفرة حالياً",  # "Expert service unavailable"
#             'error': True
#         }
    

# def text_to_speech(text):
#     """Convert text to speech using gTTS and return as base64"""
#     if not text:
#         return None

#     try:
#         lang = detect(text)
#     except:
#         lang = "en"
    
#     # Convert text to speech using gTTS
#     tts = gTTS(text=text, lang='ar' if lang == 'ar' else 'en')
    
#     with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
#         tmp_path = tmp.name
#         tts.save(tmp_path)
    
#     # Read the audio file and convert to base64
#     with open(tmp_path, 'rb') as f:
#         audio_data = f.read()
    
#     os.unlink(tmp_path)
#     return base64.b64encode(audio_data).decode('utf-8')

# @app.route('/')
# def serve_html():
#     return app.send_static_file('test1.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data.get('message')
#     audio_data = None
    
#     if data.get('audio'):
#         audio_data = base64.b64decode(data['audio'])
#         user_message = process_audio(audio_data)
    
#     bot_response = generate_response(user_message)
#     audio_response = text_to_speech(bot_response['text'])
    
#     return jsonify({
#         'response': bot_response,
#         'audio': f"data:audio/mp3;base64,{audio_response}" if audio_response else None
#     })

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
