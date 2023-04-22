import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from bs4 import BeautifulSoup

import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Have a nice day")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvic How can I help you")


def takecommand():
    # It is take microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = ''
    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print("Say that again please....")
        return 'None'
    return query
def Jarvic():
    while True:
        query = takecommand().lower()
        # Logic for executing tasks.
        if 'wikipedia' in query:
            speak('Searxching Wikipedia.....')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'hi' in query:
            speak('Hello')
        elif 'how are you' in query:
            speak('I m fine! and you?')
        elif "youtube" in query:
            webbrowser.open('youtube.com')
        elif "open google" in query:
            webbrowser.open('google.com')
        elif "stackoverflow" in query:
            webbrowser.open('stackoverflow.com')
        elif "facebook" in query:
            webbrowser.open('facebook.com')
        elif 'music' in query:
            music_dir = 'E:\\my music'
            song = os.listdir(music_dir)
            song_number = random.randrange(len(song) - 1)
            os.startfile(os.path.join(music_dir, song[song_number]))
        elif 'song' in query:
            music_dir = 'E:\\my music'
            song = os.listdir(music_dir)
            song_number = random.randrange(len(song) - 1)
            os.startfile(os.path.join(music_dir, song[song_number]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H%M%S')
            speak(f"Sir the time is {strtime}")
        elif 'pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.4\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'exit' in query:
            speak('Ok!')
            exit()
        elif 'what is your name' in query:
            speak('My name is Jarvice')
        elif 'what are you doing' in query:
            speak('Nothing')


if __name__ == "__main__":
    wishMe()
    Jarvic()