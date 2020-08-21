import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import wmi
from playsound import playsound
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import base64
import io
from tkinter import Tk, Button, Canvas, Label, Toplevel, BOTH, Text, PhotoImage, END, YES
from PIL import Image, ImageTk
from cal_setup import get_calendar_service
import pathlib
from playsound import playsound
import os
import shutil
import csv
import inflect
from io import BytesIO
from PyDictionary import PyDictionary

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
assname = "i don't know my name yet"
img = []
film_name = []


def addImage():
    # for item in img:
    #     logText.image_create(END, image=item)
    #     logText.insert(END, '\n')
    #
    for i in range(len(img)):
        logText.image_create(END, image=img[i])
        speak(film_name[i], "Assistant")


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


# def speak(msg, side):
#     if type(msg) is str:
#         addText(msg, side)
#         print("Message: " + msg)
#         separatedMsg = msg.replace(':', ' ').replace(';', ' ').split()
#         print(separatedMsg)
#         for word in separatedMsg:
#             p = inflect.engine()
#             try:
#                 print(int(word))
#                 textValue = p.number_to_words(word)
#                 msg = msg.replace(word, textValue)
#             except:
#                 pass
#         print(msg)
#         # Считывает все имеющиеся звуки
#         with open('samples/table.csv', mode='r') as infile:
#             reader = csv.reader(infile)
#             mydict = {rows[0]: rows[1] for rows in reader}
#
#         # Если текст уже синтезирован то проигрывает его
#         if mydict.get(msg.lower()):
#             playsound(f"sounds/{mydict.get(msg.lower())}.wav")
#         # Если текст не существует синтезирует его
#         else:
#             # Добавляется в текстовый файл для последущей синтезации
#             f = open("harvard_sentences.txt", "a")
#             f.truncate(0)
#             f.write("http://www.cs.columbia.edu/~hgs/audio/harvard.html\n")
#             msg = msg.lower()
#             f.write(msg)
#             f.close()
#
#             # Вызывается синтез
#             os.system("python synthesize.py")
#
#             # Подсчет сколько файлов уже синтезировано
#             cwd = os.getcwd()
#             cwd = cwd + "\sounds"
#             os.chdir(cwd)
#             print(cwd)
#             count = 0
#             for path in pathlib.Path(".").iterdir():
#                 if path.is_file():
#                     count += 1
#             print(count)
#
#             # Перенос нового файла к уже сохраненным файлам
#             cwd = cwd.replace("\sounds", "")
#             original = f'{cwd}\samples\\1.wav'
#             target = f'{cwd}\sounds\\{count + 1}.wav'
#
#             shutil.move(original, target)
#
#             # Проигрывание нового файла
#             playsound(f"{count + 1}.wav")
#
#             # Добавление файла в таблицу для последущего использования
#             os.chdir(cwd)
#             with open('samples/table.csv', 'a+', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow([msg, count + 1])
#     else:
#         totalString = ""
#         for item in msg:
#             totalString = totalString + item
#         addText(totalString, side)
#         print("Message: " + totalString)
#         for item in msg:
#             separatedMsg = item.replace(':', ' ').replace(';', ' ').split()
#             print(separatedMsg)
#             for word in separatedMsg:
#                 p = inflect.engine()
#                 try:
#                     print(int(word))
#                     textValue = p.number_to_words(word)
#                     item = item.replace(word, textValue)
#                 except:
#                     pass
#             print(item)
#             # Считывает все имеющиеся звуки
#             with open('samples/table.csv', mode='r') as infile:
#                 reader = csv.reader(infile)
#                 mydict = {rows[0]: rows[1] for rows in reader}
#
#             # Если текст уже синтезирован то проигрывает его
#             if mydict.get(item.lower()):
#                 playsound(f"sounds/{mydict.get(item.lower())}.wav")
#             # Если текст не существует синтезирует его
#             else:
#                 # Добавляется в текстовый файл для последущей синтезации
#                 f = open("harvard_sentences.txt", "a")
#                 f.truncate(0)
#                 f.write("http://www.cs.columbia.edu/~hgs/audio/harvard.html\n")
#                 item = item.lower()
#                 f.write(item)
#                 f.close()
#
#                 # Вызывается синтез
#                 os.system("python synthesize.py")
#
#                 # Подсчет сколько файлов уже синтезировано
#                 cwd = os.getcwd()
#                 cwd = cwd + "\sounds"
#                 os.chdir(cwd)
#                 print(cwd)
#                 count = 0
#                 for path in pathlib.Path(".").iterdir():
#                     if path.is_file():
#                         count += 1
#                 print(count)
#
#                 # Перенос нового файла к уже сохраненным файлам
#                 cwd = cwd.replace("\sounds", "")
#                 original = f'{cwd}\samples\\1.wav'
#                 target = f'{cwd}\sounds\\{count + 1}.wav'
#
#                 shutil.move(original, target)
#
#                 # Проигрывание нового файла
#                 playsound(f"{count + 1}.wav")
#
#                 # Добавление файла в таблицу для последущего использования
#                 os.chdir(cwd)
#                 with open('samples/table.csv', 'a+', newline='') as file:
#                     writer = csv.writer(file)
#                     writer.writerow([item, count + 1])


def speak(msg, side):
    addText(msg, side)
    engine.say(msg)
    engine.runAndWait()


def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']


def wishMe():
    global assname
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak(" Good Morning Sir !", "Assistant")
    elif 12 <= hour < 18:
        speak(" Good Afternoon Sir !", "Assistant")
    else:
        speak(" Good Evening Sir !", "Assistant")
    speak(" I am your Assistant", "Assistant")
    assname = " i dont know my name yet"
    speak(assname, "Assistant")


def usrname():
    global uname
    speak(" What should i call you sir", "Assistant")
    uname = takeCommand()
    addText(uname, "User")
    speak(" Welcome Mister", "Assistant")
    speak(" " + uname, "Assistant")


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
        # speak(str(e), "Assistant")
        speak(" Unable to Recognizing your voice.", "Assistant")
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
    # clear = lambda: os.system('cls')
    # clear()

    query = "what is antonym of word fast"
    # query = takeCommand().lower()
    addText(query, "User")

    if 'wikipedia' in query:
        speak(" Searching Wikipedia...", "Assistant")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak(" According to Wikipedia", "Assistant")
        results = re.sub("[\[].*?[\]]", "", results)
        print(results)
        speak(" " + results, "Assistant")

    elif 'open youtube' in query:
        speak(" Here you go to Youtube", "Assistant")
        url = "youtube.com"
        webbrowser.get('chrome').open(url)

    elif 'open google' in query:
        speak(" Here you go to Google", "Assistant")
        url = "google.com"
        webbrowser.get('chrome').open(url)

    elif 'open stack overflow' in query:
        speak(" Here you go to Stack Over flow.Happy coding", "Assistant")
        url = "stackoverflow.com"
        webbrowser.get('chrome').open(url)

    elif "definition" in query or "meaning" in query:
        query = query.replace("what", "").replace(" is ", "")
        query = query.replace("meaning", "").replace("definition", "").replace("of", "").replace("the", "").replace(
            "word", "")
        query = query.replace(" ", "")
        dictionary = PyDictionary()
        definitionList = dictionary.meaning(query)
        for key, value in definitionList.items():
            speak(f" As {key.lower()} it has these meanings: ", "Assistant")
            countItems = 0
            for item in value:
                countItems += 1
                item = item.replace("(", "").replace(")", "")
                speak(f" {countItems}) {item}", "Assistant")

    elif "synonym" in query:
        query = query.replace("what", "").replace(" is ", "").replace("synonym", "")
        query = query.replace("of", "").replace("the", "").replace("word", "").replace(" ", "")
        dictionary = PyDictionary()
        synonymsList = dictionary.synonym(query)
        answer = ""
        number = 0
        for item in synonymsList:
            answer = answer + item + ", "
            number += 1
            if number == 5:
                break
        answer = answer[:-2]
        speak(answer, "Assistant")

    elif "antonym" in query:
        query = query.replace("what", "").replace(" is ", "").replace("antonym", "")
        query = query.replace("of", "").replace("the", "").replace("word", "").replace(" ", "")
        dictionary = PyDictionary()
        antonymsList = dictionary.antonym(query)
        answer = ""
        number = 0
        for item in antonymsList:
            answer = answer + item + ", "
            number += 1
            if number == 5:
                break
        answer = answer[:-2]
        speak(answer, "Assistant")

    # System
    elif "set brightness to" in query:
        c = wmi.WMI(namespace='wmi')
        words = query.split()
        for word in words:
            word = word.replace('%', '')
            try:
                word = int(word)
                methods = c.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(word, 0)
                speak([" Brightness was set to", f" {word}", " percent"], "Assistant")
                # speak(f" Brightness was set to {word} percent", "Assistant")
            except Exception as e:
                pass

    elif "increase brightness" in query:
        c = wmi.WMI(namespace='wmi')
        current = c.WmiMonitorBrightness()[0]
        brightness = current.CurrentBrightness + 10
        if brightness < 100:
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)
            speak([" Brightness was increased, current brightness is", f" {brightness}"], "Assistant")
            # speak(f" Brightness was increased, current brightness is {brightness}", "Assistant")
        else:
            speak(" Brightness is maximum", "Assistant")

    elif "decrease brightness" in query:
        c = wmi.WMI(namespace='wmi')
        current = c.WmiMonitorBrightness()[0]
        brightness = current.CurrentBrightness - 10
        if brightness > 5:
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)
            speak([" Brightness was decreased, current brightness is", f" {brightness}"], "Assistant")
            # speak(f" Brightness was decreased, current brightness is {brightness}", "Assistant")
        else:
            speak(" Brightness is minimum", "Assistant")

    elif "unmute" in query:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None);
        speak(" Volume is unmuted", "Assistant")

    elif "mute" in query:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None);
        speak(" Volume is muted", "Assistant")

    elif "set volume to" in query:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        words = query.split()
        for word in words:
            word = word.replace('%', '')
            try:
                needWin = int(word)
                needDb = 25.05889 + (-65.31229 - 25.05889) / (1 + math.pow((needWin / 24.37377), (0.6767844)))
                volume.SetMasterVolumeLevel(needDb, None)
                speak([" Current volume was set to", f" {needWin}"], "Assistant")
                # speak(f" Current volume was set to {needWin}", "Assistant")
            except Exception as e:
                pass

    elif "increase volume" in query:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentDb = volume.GetMasterVolumeLevel()
        currentWin = 24.3738 * math.pow((-(90.3712 / (currentDb - 25.0589)) - 1), 1.477575428748062)
        needWin = currentWin + 10
        needDb = 25.05889 + (-65.31229 - 25.05889) / (1 + math.pow((needWin / 24.37377), (0.6767844)))
        volume.SetMasterVolumeLevel(needDb, None)
        needWin = math.trunc(needWin)
        speak([" Current volume is", f" {needWin}"], "Assistant")
        # speak(f" Current volume is {needWin}", "Assistant")

    elif "decrease volume" in query:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentDb = volume.GetMasterVolumeLevel()
        currentWin = 24.3738 * math.pow((-(90.3712 / (currentDb - 25.0589)) - 1), 1.477575428748062)
        needWin = currentWin - 10
        needDb = 25.05889 + (-65.31229 - 25.05889) / (1 + math.pow((needWin / 24.37377), (0.6767844)))
        volume.SetMasterVolumeLevel(needDb, None)
        needWin = math.trunc(needWin)
        speak([" Current volume is", f" {needWin}"], "Assistant")
        # speak(f" Current volume is {needWin}", "Assistant")

    elif 'the time' in query or 'time' in query:
        now = datetime.datetime.now()
        strTime = now.strftime("%H:%M")
        speak([" Sir, the time is", f" {strTime}"], "Assistant")
        # speak(f" Sir, the time is {strTime}", "Assistant")

    elif 'date is it' in query or 'date' in query:
        now = datetime.datetime.now()
        strTime = now.strftime("%d %B, %Y")
        speak([" Sir, the date is", f" {strTime}"], "Assistant")
        # speak(f" Sir, the date is {strTime}", "Assistant")

    # хорошая идея с открытием сторонних приложений
    # elif 'open opera' in query:
    #     codePath = r"C:\\Users\\...\\AppData\\Local\\Programs\\Opera\\launcher.exe"
    #     os.startfile(codePath)

    elif "change my name to" in query:
        query = query.replace("change my name to", "")
        uname = query

    elif "change name" in query:
        speak(" What would you like to call me, Sir ", "Assistant")
        assname = takeCommand()
        addText(assname, "User")
        speak(" Thanks for naming me", "Assistant")

    elif "what's your name" in query or "What is your name" in query:
        speak(" My friends call me", "Assistant")
        speak(" " + assname, "Assistant")
        print("My friends call me", assname)

    elif 'exit' in query:
        speak(" Thanks for giving me your time", "Assistant")
        exit()

    elif 'joke' in query:
        speak(" " + pyjokes.get_joke(), "Assistant")

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.get('chrome').open(query)
        webbrowser.open(f'https://www.google.com/search?q={query}')

    elif "who i am" in query:
        speak(" If you talk then definitely your human.", "Assistant")

    elif "why you came to world" in query:
        speak(" I came to this world to help people", "Assistant")

    elif 'is love' in query:
        speak(" It is 7th sense that destroy all other senses", "Assistant")

    elif "who are you" in query:
        speak(" I am your virtual assistant created by STEP IT Team", "Assistant")

    elif 'news' in query:
        try:
            jsonObj = urlopen('http://newsapi.org/v2/top-headlines?'
                              'country=us&'
                              'apiKey=c157fa081666455f9ff4102af7bb93cc')
            data = json.load(jsonObj)
            i = 1

            speak(" Here are some top news from the times of USA", "Assistant")
            print('''=============== TIMES OF USA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(" " + str(i) + '. ' + item['title'] + '\n', "Assistant")
                i += 1
        except Exception as e:

            print(str(e))

    elif 'lock window' in query:
        speak(" Locking the device", "Assistant")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak(" Hold On a Sec ! Your system is on its way to shut down", "Assistant")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak(" Recycle Bin Recycled", "Assistant")

    # Работать должно только в режиме безостановочной работы
    elif "don't listen" in query or "stop listening" in query:
        speak(" For how much time you want to stop me from listening commands", "Assistant")
        a = takeCommand()
        if "seconds" in a:
            a = a.split()
            for word in a:
                try:
                    number = int(word)
                    print("test")
                except:
                    pass
        elif "minutes" in a:
            a = a.split()
            for word in a:
                try:
                    number = int(word)
                    number = number * 60
                except:
                    pass
        elif "hours" in a:
            a = a.split()
            for word in a:
                try:
                    number = int(word)
                    number = number * 3600
                except:
                    pass
        elif "days" in a:
            a = a.split()
            for word in a:
                try:
                    number = int(word)
                    number = number * 86400
                except:
                    pass
        speak([" I will stop listening for", f" {number}", " seconds"], "Assistant")
        # speak(f" I will stop listening for {number} seconds", "Assistant")
        time.sleep(number)

    elif "show on map" in query or "where is" in query:
        query = query.replace("show on map", "")
        query = query.replace("where is", "")

        location = query
        speak(" User asked to Locate", "Assistant")
        speak(" " + location, "Assistant")
        webbrowser.get('chrome').open("https://www.google.nl/maps/place/" + location + "")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak(" Hibernating", "Assistant")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak(" Make sure all the application are closed before sign-out", "Assistant")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak(" What should i write, sir", "Assistant")
        note = takeCommand()
        file = open('jarvis.txt', 'w')
        speak(" Sir, Should i include date and time", "Assistant")
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
        speak(" Showing Notes", "Assistant")
        file = open("jarvis.txt", "r")
        note = file.read()
        print(note)
        speak(" " + note, "Assistant")

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
            speak([" Current temperature is:", f" {current_temperature}", " degree Celsius"], "Assistant")
            # speak(f" Current temperature is: {current_temperature} degree Celsius", "Assistant")

        else:
            speak(" City Not Found ", "Assistant")

    elif "wikipedia" in query:
        url = "wikipedia.com"
        webbrowser.get('chrome').open(url)

    elif "pick a card" in query:
        card_points = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        card_signs = ['Heart', 'CLUB', 'DIAMOND', 'SPADE']
        random_point = random.choice(card_points)
        random_sign = random.choice(card_signs)
        random_card = f"{random_point} of {random_sign}"

        speak(" " + random_card, "Assistant")

    elif "roll the dice" in query or "roll a dice" in query:
        speak(" One second", "Assistant")
        playsound("sounds/Dice.mp3")
        speak(" " + str(random.randint(1, 6)), "Assistant")

    elif "toss a coin" in query or "toss the coin" in query:
        flip = random.randint(0, 1)
        if flip == 0:
            speak(" Heads", "Assistant")
        else:
            speak(" Tails", "Assistant")

    elif "rock paper scissors" in query:
        speak(" You first!", "Assistant")
        user_choice = takeCommand()
        bot_choice = random.choice(["R", "P", "S"])
        if bot_choice == "R":
            speak(" My choice was Rock", "Assistant")
        elif bot_choice == "P":
            speak(" My choice was Paper", "Assistant")
        elif bot_choice == "S":
            speak(" My choice was Scissors", "Assistant")

        if user_choice == bot_choice:
            speak(" Draw", "Assistant")
        elif user_choice == "R":
            if bot_choice == "S":
                speak(" You won", "Assistant")
            else:
                speak(" I won", "Assistant")
        elif user_choice == "S":
            if bot_choice == "P":
                speak(" You won", "Assistant")
            else:
                speak(" I won", "Assistant")
        elif user_choice == "P":
            if bot_choice == "R":
                speak(" You won", "Assistant")
            else:
                speak(" I won", "Assistant")
        else:
            speak(" Wrong choice", "Assistant")

    elif "pick a number" in query:
        numbersRange = []
        words = query.split()
        for word in words:
            try:
                number = int(word)
                numbersRange.append(number)
            except:
                pass
        speak(" " + str(random.randint(numbersRange[0], numbersRange[1])), "Assistant")

    elif "open calendar" in query:
        service = get_calendar_service()
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        speak(" Getting upcoming events for today", "Assistant")
        events_result = service.events().list(
            calendarId='primary', timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        numberOfTodayEvents = 0

        if not events:
            speak(" No upcoming events found.", "Assistant")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            eventDate = start.split("T")
            today = now.split("T")
            if eventDate[0] == today[0]:
                numberOfTodayEvents = numberOfTodayEvents + 1
                eventTime = eventDate[1].split(":")
                speak(f" At {eventTime[0]} :{eventTime[1]} you have {event['summary']}", "Assistant")
                # print(eventTime[0] + ":" +  eventTime[1] + "    " +  event['summary'])
                # print(event)
        if numberOfTodayEvents == 0:
            speak(" No upcoming events for today found.", "Assistant")
        else:
            speak([" Total number of events for today:", f" {numberOfTodayEvents}"], "Assistant")
            # speak(f" Total number of events for today: {numberOfTodayEvents}", "Assistant")

    # most asked question from google Assistant
    elif "good morning" in query:
        speak(" A warm" + query, "Assistant")
        speak(" How are you Mister", "Assistant")

    elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
        speak(" I'm not sure about, may be you should give me some time", "Assistant")

    elif "how are you" in query:
        speak(" I'm fine, glad you me that", "Assistant")

    elif "i love you" in query:
        speak(" It's hard to understand", "Assistant")

    elif 'how are you' in query:
        speak(" I am fine, Thank you", "Assistant")
        speak(" How are you, Sir", "Assistant")

    elif 'fine' in query or "good" in query:
        speak(" It's good to know that your fine", "Assistant")

    elif "spell" in query:
        query = query.replace("spell", "")
        query = query.replace("the", "")
        query = query.replace("word", "")
        query = query.replace(" ", "")
        query = list(query)
        speak(query, "Assistant")

    elif 'convert currency' in query:
        speak(" Tell me first currency", "Assistant")
        first_currency = takeCommand()
        addText(first_currency, "User")

        speak(" Tell me second currency", "Assistant")
        second_currency = takeCommand()
        addText(second_currency, "User")

        speak(" Tell me count", "Assistant")
        value = takeCommand()
        addText(value, "User")
        value = int(value)

        try:
            url = "https://currency28.p.rapidapi.com/convert-currency"
            querystring = {"amount": value, "to": second_currency, "from": first_currency}
            headers = {
                'x-rapidapi-host': "currency28.p.rapidapi.com",
                'x-rapidapi-key': "afce3bc89fmsh1ca02613744b32ap11d006jsnda1143ee3262"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            data = json.loads(response.text)
            answer = data["result"]["value"]
            answer = float("{0:.1f}".format(answer))
            speak(f" {value} {first_currency} is {answer} {second_currency}", "Assistant")

        except Exception as e:
            print(str(e))
            speak(" Sorry, i can't do that", "Assistant")

    elif 'convert units' in query:
        speak(" Tell me first unit", "Assistant")
        first_unit = takeCommand()
        addText(first_unit, "User")

        speak(" Tell me second unit", "Assistant")
        second_unit = takeCommand()
        addText(second_unit, "User")

        speak(" Tell me count", "Assistant")
        value = takeCommand()
        addText(value, "User")
        value = int(value)

        try:
            url = "https://community-neutrino-currency-conversion.p.rapidapi.com/convert"

            payload = f"from-type={first_unit}&to-type={second_unit}&from-value={value}"
            headers = {
                'x-rapidapi-host': "community-neutrino-currency-conversion.p.rapidapi.com",
                'x-rapidapi-key': "723e3a6c9cmshc33c3107695169dp1fecb9jsn35e893aa67d4",
                'content-type': "application/x-www-form-urlencoded"
            }

            response = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response.text)
            answer = data["result"]
            speak(f" {value} {first_unit} is {answer} {second_unit}", "Assistant")
        except Exception as e:
            print(str(e))
            speak(" Sorry, i can't do that", "Assistant")

    elif "what" in query or "who" in query or "when" in query or "where" in query or "how" in query:
        app_id = "AQ36PG-QEWLVH4YKE"
        client = wolframalpha.Client(app_id)
        res = client.query(query)

        if res['@success'] == 'false':
            speak(" Question cannot be resolved", "Assistant")
        else:
            result = ''
            pod0 = res['pod'][0]
            pod1 = res['pod'][1]
            if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or (
                    pod1.get('@primary', 'false') == 'true')):
                result = resolveListOrDict(pod1['subpod'])
                speak(" " + result, "Assistant")
            else:
                answer = Toplevel()
                answer.title("display an image")
                w = 520
                h = 320
                x = 80
                y = 100
                answer.geometry("%dx%d+%d+%d" % (w, h, x, y))
                image_url = pod1["subpod"]["img"]["@src"]
                image_byt = urlopen(image_url).read()
                image_b64 = base64.encodestring(image_byt)
                photo = PhotoImage(data=image_b64)
                cv = Canvas(master=answer, bg='white')
                cv.pack(side='top', fill='both', expand='yes')
                cv.create_image(10, 10, image=photo, anchor='nw')
                answer.mainloop()

    elif "search film" in query or "film" in query or "movie" in query:
        speak(" What movie, do you want to search ?", "Assistant")
        search = takeCommand()

        try:
            url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{search}"
            PhotoUrl = ""
            headers = {
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                'x-rapidapi-key': "723e3a6c9cmshc33c3107695169dp1fecb9jsn35e893aa67d4"
            }

            response = requests.request("GET", url, headers=headers)

            data = json.loads(response.text)

            for i in range(len(data)):
                print(data["titles"][i]["title"])
                img_response = requests.get(data["titles"][i]["image"])
                img_temp = Image.open(BytesIO(img_response.content))
                img_temp = img_temp.resize((90, 120), Image.ANTIALIAS)
                img.append(ImageTk.PhotoImage(img_temp))
                film_name.append(data["titles"][i]["title"])
            addImage()

        except Exception as e:
            print(str(e))


# speak_image = PhotoImage(file="img/mic.png")
# button_speak = Button(command=turn, image=speak_image).pack()

button_speak = Button(command=turn, text="Speak").pack()

logText = Text()
logText.bind("<Key>", lambda e: "break")
logText.configure(font=20)
logText.tag_configure("user", justify="right", foreground="red")
logText.tag_configure("comp", justify="left", foreground="green")
logText.pack(expand=True, fill=BOTH)

# wishMe()
# usrname()
# speak("How can i Help you, Sir", "Assistant")


root.mainloop()
