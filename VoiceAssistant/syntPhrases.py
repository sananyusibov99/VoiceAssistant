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
from tkinter import Tk, Button, Canvas, Label, Toplevel, BOTH, Text, PhotoImage
from PIL import Image, ImageTk
from cal_setup import get_calendar_service
import pathlib
from playsound import playsound
import os
import shutil
import csv
import inflect


def synth(msg):
    print("Message: " + msg)
    separatedMsg = msg.replace(':', ' ').replace(';', ' ').split()
    print(separatedMsg)
    for word in separatedMsg:
        p = inflect.engine()
        try:
            print(int(word))
            textValue = p.number_to_words(word)
            msg = msg.replace(word, textValue)
        except:
            pass
    print(msg)
    # Считывает все имеющиеся звуки
    with open('samples/table.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader}

    # Если текст уже синтезирован то проигрывает его
    if mydict.get(msg.lower()):
        pass
        #playsound(f"sounds/{mydict.get(msg.lower())}.wav")
    # Если текст не существует синтезирует его
    else:
        # Добавляется в текстовый файл для последущей синтезации
        f = open("harvard_sentences.txt", "a")
        f.truncate(0)
        f.write("http://www.cs.columbia.edu/~hgs/audio/harvard.html\n")
        msg = msg.lower()
        f.write(msg)
        f.close()

        # Вызывается синтез
        os.system("python synthesize.py")

        # Подсчет сколько файлов уже синтезировано
        cwd = os.getcwd()
        cwd = cwd + "\sounds"
        os.chdir(cwd)
        print(cwd)
        count = 0
        for path in pathlib.Path(".").iterdir():
            if path.is_file():
                count += 1
        print(count)

        # Перенос нового файла к уже сохраненным файлам
        cwd = cwd.replace("\sounds", "")
        original = f'{cwd}\samples\\1.wav'
        target = f'{cwd}\sounds\\{count + 1}.wav'

        shutil.move(original, target)

        # Проигрывание нового файла
        #playsound(f"{count + 1}.wav")

        # Добавление файла в таблицу для последущего использования
        os.chdir(cwd)
        with open('samples/table.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([msg, count + 1])


# Синтезация файлов с цифрами до 100
for var in range(100):
    synth(str(var))

# Наиболее часто используемые фразы
phrases = [" Good Morning Sir !", " Good Afternoon Sir !", " Good Evening Sir !", " I am your Assistant",
           " i dont know my name yet", " What should i call you sir", " Welcome Mister",
           " Unable to Recognizing your voice.", " Searching Wikipedia...",
           " According to Wikipedia", " Here you go to Youtube", " Here you go to Google",
           " Here you go to Stack Over flow.Happy coding", " Brightness is maximum",
           " Brightness is minimum", "Volume is unmuted", " Volume is muted",
           " What would you like to call me, Sir ", " Thanks for naming me", " My friends call me",
           " Thanks for giving me your time", " If you talk then definitely your human.",
           " I came to this world to help people", " It is 7th sense that destroy all other senses",
           " I am your virtual assistant created by STEP IT Team", " Here are some top news from the times of USA",
           " Locking the device", " Hold On a Sec ! Your system is on its way to shut down", " Recycle Bin Recycled",
           " For how much time you want to stop me from listening commands", " User asked to Locate",
           " Hibernating", " Make sure all the application are closed before sign-out",
           " What should i write, sir", " Sir, Should i include date and time", " Showing Notes", " City name ",
           " City Not Found ", " Question cannot be resolved", " One second", " Heads", " Tails",
           " Getting upcoming events for today", " No upcoming events found.", " No upcoming events for today found.",
           " A warm", " How are you Mister", " I'm not sure about, may be you should give me some time",
           " I'm fine, glad you me that", " It's hard to understand", " I am fine, Thank you", " How are you, Sir",
           " It's good to know that your fine", " Tell me first currency", " Tell me second currency",
           " Tell me count", " Sorry, i can't do that", " Tell me first unit", " Tell me second unit", " Tell me count",
           " What movie, do you want to search ?", " There is movies, i founded", " Brightness", " percent",
           " Brightness was increased, current brightness is", " Brightness was decreased, current brightness is",
           " Current volume was set to", " Current volume is", " Sir, the time is", " Sir, the date is",
           " I will stop listening for", " seconds", " Current temperature is:", " degree Celsius",
           " Total number of events for today:", " Brightness was set to", " You first!", " My choice was Rock",
           " My choice was Paper", " My choice was Scissors", " Draw", " You won", " I won", " Wrong choice"]

for item in phrases:
    synth(item)