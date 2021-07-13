import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak ("Good evening")
    else:
        speak("Good night")

    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing........")
        query = r.recognize_google(audio, language = 'en-US')
    except Exception as e:
        print(e)
        speak("Say that again please.......")
        return "None"
    return query

if __name__ == "__main__":
    greet()


    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
             time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia ", "")
            print(query)
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "thank you" in query or "bye" in query or "offline" in query:
            quit()
