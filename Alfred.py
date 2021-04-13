import pyttsx3
import datetime
import  speech_recognition as sr
import wikipedia
import  webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Master Wayne')
    elif hour <= 12 and hour < 12:
        speak("Good Afternoon Master Wayne")
    else:
        speak("Good Evening Master Wayne")
    speak("How May I Help You Sir")

def takeCommand():
    # Take Microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listining...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again Please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('jerrytyagi4@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        '''Logic for excuting task based on query'''
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipesia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'play music' in query:
            music_dir = 'E:\\Set'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time_str}")

        elif 'open cose' in query:
            code_path = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open spotify' in query:
            spotify_path = "C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify_path)
        elif 'email to jerry' in query:
            try:
                speak("What Should i Say")
                content = takeCommand()
                to = "jerrytyagi4@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send email")
