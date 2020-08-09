import subprocess
import wolframalpha
import pyttsx3
from tkinter import *
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

root = Tk()
root.title("Voice Assistant")
root.minsize(500, 500)
global assname
assname = ("i dont know my name yet")

def deleteText(msg, side):
    logText.configure(state='normal')
    logText.delete(f"[{side}]: " + msg, 'end')
    logText.configure(state='disabled')
    root.update()


def addText(msg, side):
    logText.configure(state='normal')
    text = f"[{side}]: " + msg + "\n"
    if side == "Assistant":
        logText.insert("end", text, "comp")
    elif side == "User":
        logText.insert("end", text, "user")
    logText.configure(state='disabled')
    root.update()


def speak(msg, side):
    addText(msg, side)
    engine.say(msg)
    engine.runAndWait()


def wishMe():
    global assname
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !", "Assistant")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !", "Assistant")
    else:
        speak("Good Evening Sir !", "Assistant")
    speak("I am your Assistant", "Assistant")
    assname = ("i dont know my name yet")
    speak(assname, "Assistant")


def usrname():
    global uname
    speak("What should i call you sir", "Assistant")
    uname = takeCommand()
    addText(uname, "User")
    speak("Welcome Mister", "Assistant")
    speak(uname, "Assistant")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        addText("Listening...", "Assistant")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # deleteText("Listening...", "Assistant")
        addText("Recognizing...", "Assistant")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak(str(e), "Assistant")
        speak("Unable to Recognizing your voice.", "Assistant")
        return "None"

    return query


# Надо проверить
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


def turn():
        global uname
        global assname
        #clear = lambda: os.system('cls')

        #clear()


        query = takeCommand().lower()
        addText(query, "User")

        # Надо убрать [] в результатах ответов (транскрипцию, она звучит ужасно)
        # Взять results и вырезать часть строки с []
        if 'wikipedia' in query:
            speak('Searching Wikipedia...', "Assistant")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia", "Assistant")
            print(results)
            speak(results, "Assistant")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n", "Assistant")
            url = "youtube.com"
            webbrowser.get('chrome').open(url)

        elif 'open google' in query:
            speak("Here you go to Google\n", "Assistant")
            url = "google.com"
            webbrowser.get('chrome').open(url)

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding", "Assistant")
            url = "stackoverflow.com"
            webbrowser.get('chrome').open(url)

        elif 'the time' in query:
            now = datetime.datetime.now()
            strTime = now.strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}", "Assistant")

        elif 'date is it' in query:
            now = datetime.datetime.now()
            strTime = now.strftime("%d %B, %Y")
            speak(f"Sir, the date is {strTime}", "Assistant")

        # хорошая идея с открытием сторонних приложений
        # elif 'open opera' in query:
        #     codePath = r"C:\\Users\\...\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        #     os.startfile(codePath)

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ", "Assistant")
            assname = takeCommand()
            addText(assname, "User")
            speak("Thanks for naming me", "Assistant")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me", "Assistant")
            speak(assname, "Assistant")
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time", "Assistant")
            exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke(), "Assistant")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.get('chrome').open(query)
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif "who i am" in query:
            speak("If you talk then definately your human.", "Assistant")
        elif "why you came to world" in query:
            speak("I came to this world to help people", "Assistant")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses", "Assistant")

        elif "who are you" in query:
            speak("I am your virtual assistant created by STEP IT Team", "Assistant")

        elif 'news' in query:
            try:
                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?'
                                   'country=us&'
                                   'apiKey=c157fa081666455f9ff4102af7bb93cc')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of USA', "Assistant")
                print('''=============== TIMES OF USA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n', "Assistant")
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device", "Assistant")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down", "Assistant")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled", "Assistant")

        #Нужно переделать добавить возможность делать задержку на несколько минут (если в строке есть слово минута, то умножать время на 60)
        #Работать должно только в режиме безостановочной работы
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands", "Assistant")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate", "Assistant")
            speak(location, "Assistant")
            webbrowser.get('chrome').open("https://www.google.nl/maps/place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating", "Assistant")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out", "Assistant")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir", "Assistant")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time", "Assistant")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                now = datetime.datetime.now()
                strTime = now.strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes", "Assistant")
            file = open("jarvis.txt", "r")
            note = file.read()
            print(note)
            speak(note, "Assistant")

        elif "weather" in query:
            # Google Open weather website
            # to get API of Open weather
            api_key = "44e4a0d8152c6a9538668064c5c591dc"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ", "Assistant")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
            print(complete_url)
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in Celsius unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))
                speak(f"Current temperature is: {current_temperature} degree Celsius", "Assistant")
                #speak("", "Assistant")

            else:
                speak(" City Not Found ", "Assistant")

        elif "wikipedia" in query:
            url = "wikipedia.com"
            webbrowser.get('chrome').open(url)

        elif "good morning" in query:
            speak("A warm" + query, "Assistant")
            speak("How are you Mister", "Assistant")

        # most asked question from google Assistant
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about, may be you should give me some time", "Assistant")
        elif "how are you" in query:
            speak("I'm fine, glad you me that", "Assistant")
        elif "i love you" in query:
            speak("It's hard to understand", "Assistant")

        elif 'how are you' in query:
            speak("I am fine, Thank you", "Assistant")
            speak("How are you, Sir", "Assistant")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine", "Assistant")


speak_image = PhotoImage(file="img/mic.png")
button_speak = Button(command=turn, image=speak_image).pack()

logText = Text(height=50, width=50)
logText.bind("<Key>", lambda e: "break")
logText.configure(font=20)
logText.tag_configure("user", justify="right", foreground="red")
logText.tag_configure("comp", justify="left", foreground="green")
logText.pack()

wishMe()
usrname()
speak("How can i Help you, Sir", "Assistant")


root.mainloop()