from urllib import request
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests, json
from googlesearch import search

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
    speak("Welcome back Anoushka!")
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
        query = r.recognize_google(audio, language = 'en-CA')
    except Exception as e:
        print(e)
        speak("Say that again please.......")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/anous/Desktop/AIVoice/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    speak("Battery is at: "+ str(battery.percent)+"%")

def jokes():
    speak(pyjokes.get_joke())

def open_website(query):
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    for j in search(query, tld="com", num=10, stop=1, pause=2):
        wb.get(chromepath).open_new_tab(j)

def weather():
    api_key = "" #can get in https://openweathermap.org/price
    url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Which city are you looking for?")
    city = takeCommand().lower()
    complete_url = url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x['cod'] != "404":
        y = x['main']
        temperature = round(y['temp'] - 273.15)
        pressure = y["pressure"]
        humidity = y["humidity"]
        weather_description = x["weather"][0]["description"]
        speak("The current weather in " + city + " is " + str(temperature) + " degrees celcius with atmospheric pressure at " + str(pressure) +
         " hPa and humidity at " + str(humidity) + " percentage. One word to describe: " + str(weather_description))
    else:
        speak("Say that again please.......")

if __name__ == "__main__":
    greet()

    while True:
        query = takeCommand().lower()

        if "time" in query: #time feature
             time()
        elif "date" in query: #date feature
            date()
        elif "wikipedia" in query: #search in wikipedia feature
            speak("Searching")
            query = query.replace("wikipedia ", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "open" in query: #opening a website 
            speak("Opening " + query.replace("open ", ""))
            open_website(query.replace("open ", ""))
        elif "log out" in query: #log out from computer
            os.system("shutdown - l")
        elif "shutdown" in query: #shut down computer
            os.system("shutdown /s /t 1")
        elif "restart" in query: #restart computer
            os.system("shutdown /r /t 1")
        elif "play songs" in query: #play music in the system
            songs_dir = "C:/Users/Default/Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remind" in query: #put things to remember
            speak("What should I remember?")
            data = takeCommand()
            speak("remember: " + data)
            remember = open("data.txt", "a")
            currdate = datetime.datetime.now().date()
            remember.write(currdate.strftime('%B %d, %Y') + ": " + data +"\n")
            remember.close()
        elif "do you remember anything" in query: #reads out what is remembered
            remember = open("data.txt", "r")
            lines = remember.readlines()
            speak("Why yes ofcourse, I do remember the following:")
            for line in lines:
                speak(line.strip())
        elif "screenshot" in query: #takes a screenshot
            screenshot();
            speak("Screenshot complete")
        elif "cpu" in query: #says the cpu and battery percentage of the computer
            cpu()
        elif "joke" in query: #says a joke
            jokes()
        elif "weather" in query: #weather features
            weather()
        elif "thank you" in query or "deactivates" in query: #deactives the AI
            quit()
