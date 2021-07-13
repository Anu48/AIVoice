import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 -> male voice; 1 -> female voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello")
