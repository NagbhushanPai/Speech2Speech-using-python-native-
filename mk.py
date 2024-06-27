import speech_recognition as spr
import googletrans
from googletrans import Translator
import pyttsx3

# Importing necessary modules required


# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mc = spr.Microphone()



# Translator method for translation
translator = Translator()

#  print(googletrans.LANGUAGES)  to get all the languages


# short form of english in which you will speak


from_lang = 'en'

# In which we want to convert, short form of hindi
to_lang = 'hi'

with mc as source:
    
    print("Speak a stentence...")
    recog1.adjust_for_ambient_noise(source, duration=0.2)
    
    # Storing the speech into audio variable
    audio = recog1.listen(source)
    
    # Using recognize.google() method to
    # convert audio into text
    get_sentence = recog1.recognize_google(audio)

    # Using try and except block to improve
    # its efficiency.
    try:
        
        # Printing Speech which need to 
        # be translated.
        print("Phrase to be Translated :" + get_sentence)

        text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)

        engine = pyttsx3.init()
        engine.say(get_sentence)
        engine.say(text_to_translate.text)
        engine.runAndWait()

    except spr.UnknownValueError:
        print("Unable to Understand the Input")
        
    except spr.RequestError as e:
        print("Unable to provide Required Output".format(e))

