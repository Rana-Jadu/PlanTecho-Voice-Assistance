import os
import speech_recognition as sr
import pyttsx3
from langdetect import detect
import google.generativeai as genai
import threading

# Load API Key from environment variables
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("Missing API key. Set GEMINI_API_KEY as an environment variable.")

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize Text-to-Speech engine with Arabic support
def setup_tts():
    engine = pyttsx3.init()
    # Try to find Arabic voice
    voices = engine.getProperty('voices')
    arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
    if arabic_voices:
        engine.setProperty('voice', arabic_voices[0].id)
    return engine

tts_engine = setup_tts()

# Enhanced Speech Recognition Function with unlimited listening time
def recognize_speech():
    """Recognizes speech input from the user in Arabic or English without time constraints."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Speak Arabic prompt
        tts_engine.say("تحدث الآن، أنا أستمع إليك")  # "Speak now, I'm listening to you"
        tts_engine.runAndWait()
        print("Listening... (Arabic/English)")
        
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 1.5  # Wait longer for speech to end
        
        try:
            # Remove timeout parameter for unlimited listening
            audio = recognizer.listen(source)
            try:
                # First try Arabic recognition
                text = recognizer.recognize_google(audio, language="ar-EG")
                print(f"You said (Arabic): {text}")
                return text
            except:
                # Fallback to English if Arabic fails
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"You said (English): {text}")
                return text
        
        except sr.UnknownValueError:
            error_msg = "لم أستطع فهم ما قلته"  # "I couldn't understand what you said"
            tts_engine.say(error_msg)
            tts_engine.runAndWait()
            return None
        except sr.RequestError:
            error_msg = "حدث خطأ في الاتصال بالخدمة"  # "Service connection error"
            tts_engine.say(error_msg)
            tts_engine.runAndWait()
            return None

# Language Detection Function
def detect_language(text):
    """Detects the language of the user's input."""
    try:
        return detect(text)
    except:
        return "unknown"

# Generating Response Function with Arabic support
def ask_gemini(user_input):
    """Ensures Gemini responds ONLY to plant-related questions in the detected language."""
    
    # Detect language of the input
    lang = detect_language(user_input)

    # Define the prompt for Gemini AI
    prompt = (
        "You are a plant expert. Answer ONLY plant-related questions. "
        "Respond in the same language as the question. "
        "If the question is about plants, provide a detailed response. "
        "If not, reply with: 'I only answer plant-related questions.'\n\n"
        f"User question: {user_input}"
    )

    try:
        # Speak processing message in the detected language
        processing_msg = "جارٍ المعالجة" if lang == "ar" else "Processing"
        tts_engine.say(processing_msg)
        tts_engine.runAndWait()
        
        response = model.generate_content(prompt)
        
        if not response or not hasattr(response, 'text'):
            error_msg = "لا يمكنني الحصول على المعلومات الآن"  # "Can't get information now"
            tts_engine.say(error_msg)
            tts_engine.runAndWait()
            return error_msg
        
        response_text = response.text
        
        # Speak the response
        speak_response(response_text, lang)
        return response_text
    
    except Exception as e:
        error_msg = f"حدث خطأ: {str(e)}" if lang == "ar" else f"Error: {str(e)}"
        tts_engine.say(error_msg)
        tts_engine.runAndWait()
        return error_msg
    
# Enhanced Reading Response Function
def speak_response(text, lang):
    """Converts text to speech based on detected language."""
    # Set appropriate voice if available
    voices = tts_engine.getProperty('voices')
    if lang == "ar":
        arabic_voices = [v for v in voices if 'arabic' in v.name.lower() or 'ar-' in v.id.lower()]
        if arabic_voices:
            tts_engine.setProperty('voice', arabic_voices[0].id)
    
    # Split long responses into chunks to prevent buffer overflow
    max_chars = 200  # Adjust based on your TTS engine's limits
    chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
    
    for chunk in chunks:
        tts_engine.say(chunk)
        tts_engine.runAndWait()

if __name__ == "__main__":
    while True:
        user_question = recognize_speech()
        if user_question:
            bot_response = ask_gemini(user_question)
            print(f"\nGemini Response: {bot_response}")
        
        # Continue or quit
        tts_engine.say("اضغط زر الإدخال للمتابعة أو اكتب خروج للإنهاء")
        tts_engine.runAndWait()
        user_input = input("\nPress Enter to continue or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            tts_engine.say("مع السلامة")  # "Goodbye"
            tts_engine.runAndWait()
            break
