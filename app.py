import os
import re
import speech_recognition as sr
import pyttsx3
from flask import Flask, render_template, send_from_directory
import wikipedia
import datetime

app = Flask(__name__)

def recognize_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, timeout=20)
        print("Recognizing...")
    return recognizer.recognize_google(audio).lower()

def play_on_YT(song_name):
    try:
        import pywhatkit
        search_results = pywhatkit.playonyt(song_name)
        video_id = search_results[0]['link']
        return render_template('play_youtube.html', video_id=video_id)

    except Exception as e:
        print(f"Error searching for the song: {e}")
        return "Error searching for the song", 500
    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/voice_command', methods=['POST'])
def voice_command():
    try:
        command = recognize_audio()

        if "play on youtube"  in command:
            song = re.search(r'play on youtube (.+)', command).group(1).strip()
            return play_on_YT(song)
        
        elif "play" in command:
            song = re.search(r'play (.+)', command).group(1).strip()
            return play_on_YT(song)

        elif any(keyword in command for keyword in ["tell me about", "search for", "who is", "what is"]):
            person = command.replace("tell me about", '').strip()
            info = wikipedia.summary(person, sentences=2)
            result = f"search: {info}"
            #print(info)
            #speak(info)

        elif 'time right now' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            result = f"date {time}"
            speak('current time is ' + time)

        elif "day today" or 'today is' in command:
            day = datetime.datetime.now().strftime('%A')
            result = f"Day: {day}"

        elif "how are you" in command:
            result="I am doing great how can i help you"
            speak("I am doing great how can i help you")

        else:
            result = "Command not recognized"

        speak(result)

    except sr.UnknownValueError:
        result = "Sorry, could not understand the audio."
    except sr.WaitTimeoutError:
        result = "Listening timed out. Please try again."
    except Exception as e:
        result = f"Error: {e}"

    return result

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    app.run(debug=True)
