import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alfred, always at your service. Tell me Sir, how may i help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak("opening...")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("opening...")
            webbrowser.open("facebook.com")

        elif 'open github' in query:
            speak("opening...")
            webbrowser.open("github.com")

        elif 'open linkedin' in query:
            speak("opening...")
            webbrowser.open("linkedin.com")

        elif 'open twitter' in query:
            speak("opening...")
            webbrowser.open("twitter.com")

        elif 'open youtube' in query:
            speak("opening...")
            webbrowser.open("youtube.com")

        elif 'open music' in query:
            speak("opening...")
            webbrowser.open("music.youtube.com")

        elif 'play song' in query:
            speak("Playing...")

            music_dir = 'D:\\WEBDEV\\Spotify clone\\songs'

            songs = os.listdir(music_dir)

            print(songs)

            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("opening...")
            codePath = "C:\\Users\\SUPRIYO SAHA\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open browser' in query:
            speak("opening...")
            browserPath = "C:\\Users\\SUPRIYO SAHA\\Desktop\\Microsoft Edge.lnk"
            os.startfile(browserPath)

        elif 'who are you' in query:
            speak("Hello! I am Alfred your virtual assistant! I can automate various tasks just by your given commands")

        elif 'hello' in query:
            speak("Hello sir! How was your day?")

        elif 'take a break' in query:
            speak("Terminating sir, have a nice day...")
            exit()
