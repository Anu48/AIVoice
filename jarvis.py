import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 -> male voice; 1 -> female voice
newVoiceRate = 190 #default: 200 watts per minute
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is " + time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def greet():
    speak("Welcome back! I'm Iris.")
    date()
    time()
    speak("How can I help you?")

# speak("Hello! I'm Iris. How can I help you?")
# time()
greet()
