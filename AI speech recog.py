import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from urllib.request import urlopen
import json
import time
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...");    
        query = r.recognize_google(audio, language='en-in');
        print(f"User said: {query}\n");

    except Exception as e:
        # print(e)    
        print("Say that again please...");  
        return "None";
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('keshavchatterjee72@gmail.com', 'keshav1122')
    server.sendmail('chetanmehta2001@gmail.com', to, content)
    server.close()

if _name_ == "_main_":
    wishMe()
    while True:
        if 1:
            query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query: 
            webbrowser.open("wikipedia.com")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KESHAV\\Desktop\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\KESHAV\\testfile.py"
            os.startfile(codePath)

        elif 'send email' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'jarvis stop' in query:
            exit()
        elif 'search for' in query:
           webbrowser.open("google.com")
        elif 'hi jarvis' in query:
            speak("Hello Sir")
        elif 'how are you' in query:
            speak("Excellent ,how are you")
        elif 'what do you like' in query:
            speak("I like learning new things")   
        elif 'who are you' in query:
            speak("I am Ai voice assistant and i am here to help you")