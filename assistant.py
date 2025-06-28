import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def talk(text):
    print("🎙️ Sai:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_sai():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing  on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what is the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "what is" in command or "who is" in command or "tell me about" in command:
        try:
            topic = command.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
            info = wikipedia.summary(topic, sentences=2)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk(f"That could refer to many things: {e.options[0]}")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find anything about that.")
        except Exception:
            talk("Something went wrong while searching.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()
    
    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")

talk("Yo! I'm SAI – your personal voice assistant 💡")
while True:
    run_sai()
