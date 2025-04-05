import os
import threading
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator

# GUI Setup
win = tk.Tk()
win.geometry("700x500")
win.title("🔊 AI-Powered Voice & Text Translator 📱🗣️💬🤖")
icon = tk.PhotoImage(file="icon.png")
win.iconphoto(False, icon)



down_arrow = tk.Label(win, text="▼")
down_arrow.pack()


# Language Options
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

language_names = list(language_codes.keys())

# Input Language
input_lang_label = tk.Label(win, text="Select Input Language:")
input_lang_label.pack()
input_lang = ttk.Combobox(win, values=language_names)
input_lang.set("English")
input_lang.pack()
input_lang.bind("<<ComboboxSelected>>", lambda e: update_input_lang_code(e))
if input_lang.get() == "":
    input_lang.set("auto")

# Output Language
output_lang_label = tk.Label(win, text="Select Output Language:")
output_lang_label.pack()
output_lang = ttk.Combobox(win, values=language_names)
output_lang.set("Spanish")
output_lang.pack()
output_lang.bind("<<ComboboxSelected>>", lambda e: update_output_lang_code(e))

def translate_text(text):
    source_lang = language_codes.get(input_lang.get(), "auto")  # Default to "auto" for input
    target_lang = language_codes.get(output_lang.get(), "en")   # Default to "en" for output
    return GoogleTranslator(source=source_lang, target=target_lang).translate(text)

import tempfile  # Add this import

def translate_and_speak(text):
    if not text:
        return
    
    translated_text = translate_text(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)

    try:
        # Use a temporary file to avoid permission issues
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            audio_file = temp_audio.name  # Get the temporary file path
            tts = gTTS(translated_text, lang=language_codes[output_lang.get()])
            tts.save(audio_file)  # Save to temp file
            
        threading.Thread(target=playsound, args=(audio_file,)).start()  # Play the saved audio
    except Exception as e:
        print(f"Error saving or playing audio: {e}")


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        input_text.delete("1.0", tk.END)
        output_text.delete("1.0", tk.END)
        try:
            print("Listening...")
            audio = r.listen(source)
            recognized_text = r.recognize_google(audio, language=language_codes[input_lang.get()])
            input_text.insert(tk.END, recognized_text)  # Show recognized text
            translate_and_speak(recognized_text)  # Translate and speak output
        except sr.UnknownValueError:
            input_text.insert(tk.END, "Could not understand speech.")
        except sr.RequestError:
            input_text.insert(tk.END, "Error with speech recognition service.")

def text_to_speech():
    user_input = input_text.get("1.0", tk.END).strip()
    if user_input:
        translate_and_speak(user_input)

def update_input_lang_code(event):
    selected_language_name = event.widget.get()
    if selected_language_name in language_codes:
        input_lang.set(selected_language_name)


def update_output_lang_code(event):
    selected_language_name = event.widget.get()
    if selected_language_name in language_codes:
        output_lang.set(selected_language_name)


def update_translation():
    text_to_speech()

def run_translator():
    win.mainloop()

def kill_execution():
    win.destroy()

def open_about_page():
    about_win = tk.Toplevel(win)
    about_win.title("About")
    about_label = tk.Label(about_win, text="Voice & Text Translator\nVersion 1.0")
    about_label.pack()

def open_webpage():
    os.system("start https://www.google.com")

# Recognized & Translated Text Areas
input_text_label = tk.Label(win, text="Recognized/Entered Text:")
input_text_label.pack()
input_text = tk.Text(win, height=3, width=50)
input_text.pack()

output_text_label = tk.Label(win, text="Translated Text:")
output_text_label.pack()
output_text = tk.Text(win, height=3, width=50)
output_text.pack()

# Buttons
speech_button = tk.Button(win, text="🎤 Speak & Translate", command=speech_to_text)
speech_button.pack()

text_button = tk.Button(win, text="📝 Translate Text", command=text_to_speech)
text_button.pack()


win.mainloop()
