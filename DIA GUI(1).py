#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pyttsx3
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
from time import sleep
from threading import Thread
from sys import exit
import time
import playsound
import speech_recognition as sr
import mysql.connector as sql
import random
import pandas as pd
import webbrowser  
import pyjokes 
import subprocess 
import os
import pandas as pd
import csv
import wikipedia 
import wolframalpha
import winshell
import json
import feedparser
import smtplib
import datetime 
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import randfacts

from tkinter import *
import tkinter as tk
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from playsound import playsound

voiceEngine = pyttsx3.init()
# rate
voiceEngine.setProperty('rate', 150)
# voice
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak(text):
    AITaskStatusLbl['text'] = 'Speaking...'
    voiceEngine.say(text)
    voiceEngine.runAndWait()
    
def takeCommand():
    print('\nListening...')
    AITaskStatusLbl['text'] = 'Listening...'
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

        try:
            print("Recognizing the command")
            AITaskStatusLbl['text'] = 'Processing...'
            command = recog.recognize_google(userInput, language ='en-in')
            print(f"Command is: {command}\n")
            

        except Exception as e:
            print(e)
            print("Unable to Recognize the voice.")
            return "None"

    return command


def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("I am glad to know you!")
    speak(uname)
    #columns = shutil.get_terminal_size().columns
    #speak("How can i Help you, ")

def wish():
        print("Wishing.")
        time = int(datetime.datetime.now().hour)
        global uname,asname
        if time>= 0 and time<12:
            speak("Good Morning!")

        elif time<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        asname ="DIVA"
        speak("I am your Voice Assistant")
        speak(asname)
        print("I am your Voice Assistant,",asname)
        
def prog_exit():
    speak("Thanks for giving me your time")
    AITaskStatusLbl['text'] = 'Offline'
    exit()

def getNews():
    try:
        response = requests.get('https://www.bbc.com/news')

        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']

        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                print(x.text.strip())
    except Exception as e:
        print(str(e))

def callVoiceAssistant():
    uname=''
    asname=''
    #response = ''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:
        for j in range(5):   
            speak("What can I do for you")
            command = takeCommand().lower()
            print(command)
            if command:
                break
            if not command:
                break
            speak("Sorry. I didn't catch that. What did you say?")
            print("I didn't catch that. What did you say?\n")


        if "DIVA" in command:
            wish()

        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)
            
        elif "that is all" in command or 'nothing' in command:
            speak("Great to be of service!")
            speak("Do you want to hear something interesting?")
            response = takeCommand()
            if 'yes' in response or 'sure' in response:
                speak(randfacts.get_fact(False))
                time.sleep(2)
                speak("I hope that added more to your knowledge!")
            elif 'no' in response or 'not really' in response:
                speak("Too bad, I had an interesting fact to tell you. Next time then.")
                prog_exit()

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" +command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
            
        elif 'question' in command:
            print("What is your question")
            speak("Sure, What is your question?")
            question = takeCommand()
            app_id = "9UWXW5-LGXGJQPK25"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "who are you" in command:
            speak("I am your virtual assistant, DIVA, I thought you already knew.")

        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)

        elif "interesting" in command:
            speak(randfacts.get_fact(False))

        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            asname = takeCommand()
            speak("Thank you for naming me!")

        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)

        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 3)
            #results=webbrowser.open("wikipedia.com")
            speak("These are the results from Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("Opening Youtube\n")
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open_new_tab("https://www.google.com")

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'exit' in command or 'terminate' in command or 'end' in command:
            prog_exit()

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif 'news' in command:
            getNews()

        elif "don't listen" in command or "stop listening" in command:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)


        elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in command:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")

        
        else:
            speak("Sorry, I am not able to understand you")
    
# Create an instance of tkinter window
from tkinter import *
import tkinter as tk
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
from playsound import playsound

global screen
screen = Tk()
screen.title("Diva")
screen.geometry("300x290")

def start_assistant(event):
    try:
        Thread(target=callVoiceAssistant).start()  
    except:
        pass
    
def close(event):
     screen.destroy()
    
screen.configure(bg='black') 

frame = LabelFrame(screen)
frame.pack()
frame.place(anchor='s', relx=0.5, rely=1.0)

#load the image onto the button
mic_image = Image.open('diva_ai.png')
mic_image = mic_image.resize((300,250), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(mic_image)

microphone_button = Button(frame,image=my_img)
microphone_button.bind('<Return>', start_assistant)
microphone_button.focus()
microphone_button.pack(expand=True)

# exit_button = Button(frame)
# exit_button.bind('<Escape>', close)
# exit_button.focus()
# exit_button.pack(expand=True)

#Attach label onto the GUI to show the different processes
AITaskStatusLbl = Label(frame,text='Offline', fg='grey', font=('montserrat', 16))
AITaskStatusLbl.pack()

screen.mainloop()

