import speech_recognition as spr
from googletrans import Translator
import pyttsx3

def recognize_speech(recognizer, microphone):
    """Recognize speech using the microphone."""
    with microphone as source:
        print("Speak a sentence...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
    return audio

def translate_text(translator, text, src_lang, dest_lang):
    """Translate text from source language to destination language."""
    return translator.translate(text, src=src_lang, dest=dest_lang).text

def text_to_speech(engine, text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def main():
    # Initialize recognizer, microphone, translator, and text-to-speech engine
    recognizer = spr.Recognizer()
    microphone = spr.Microphone()
    translator = Translator()
    tts_engine = pyttsx3.init()

    # Define source and target languages
    from_lang = 'en'  # English
    to_lang = 'hi'    # Hindi

    try:
        # Recognize speech
        audio = recognize_speech(recognizer, microphone)
        get_sentence = recognizer.recognize_google(audio)
        print("Phrase to be Translated: " + get_sentence)

        # Translate text
        translated_text = translate_text(translator, get_sentence, from_lang, to_lang)
        print("Translated Phrase: " + translated_text)

        # Convert text to speech
        text_to_speech(tts_engine, get_sentence)
        text_to_speech(tts_engine, translated_text)

    except spr.UnknownValueError:
        print("Unable to understand the input.")
    except spr.RequestError as e:
        print(f"Unable to provide required output: {e}")

if __name__ == "__main__":
    main()
