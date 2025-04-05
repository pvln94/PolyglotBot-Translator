from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from playsound import playsound
import tempfile
import threading
from deep_translator import GoogleTranslator

app = Flask(__name__)

language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Marathi": "mr",
    "Malayalam": "ml",
    "Urdu": "ur",
    "Arabic": "ar",
    "Italian": "it",
    "Portuguese": "pt",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Hebrew": "he",
    "Thai": "th",
    "Vietnamese": "vi",
    "Swedish": "sv",
    "Polish": "pl",
    "Hungarian": "hu",
    "Czech": "cs",
    "Romanian": "ro",
    "Filipino": "tl",
    "Indonesian": "id"
}

# Convert text to speech and play it
def translate_and_speak(text, output_lang_code):
    if not text:
        return
    translated_text = GoogleTranslator(source="auto", target=output_lang_code).translate(text)
    try:
        # Use a temporary file to avoid permission issues
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            audio_file = temp_audio.name  # Get the temporary file path
            tts = gTTS(translated_text, lang=output_lang_code)
            tts.save(audio_file)  # Save to temp file
            
        threading.Thread(target=playsound, args=(audio_file,)).start()  # Play the saved audio
    except Exception as e:
        print(f"Error saving or playing audio: {e}")

# Web page
@app.route('/')
def index():
    return render_template('index.html', languages=language_codes.keys())

# Handle form submission for translation and speech
@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    input_lang = request.form['input_lang']
    output_lang = request.form['output_lang']
    output_lang_code = language_codes.get(output_lang, 'en')

    translated_text = GoogleTranslator(source=language_codes.get(input_lang, 'auto'), target=output_lang_code).translate(input_text)

    translate_and_speak(translated_text, output_lang_code)  # Speak the translated text

    return jsonify({'translated_text': translated_text})

# Handle speech recognition, translation, and text-to-speech
@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():
    recognized_text = request.json.get('speech_text', '')
    output_lang = request.json.get('output_lang', 'en')
    output_lang_code = language_codes.get(output_lang, 'en')

    if recognized_text:
        # Translate the recognized text
        translated_text = GoogleTranslator(source="auto", target=output_lang_code).translate(recognized_text)
        # Convert translated text to speech
        translate_and_speak(translated_text, output_lang_code)
        return jsonify({'translated_text': translated_text, 'recognized_text': recognized_text})
    else:
        return jsonify({'error': 'No speech input recognized'})

if __name__ == "__main__":
    app.run(debug=True)
