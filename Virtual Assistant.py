import speech_recognition as sr # pip install SpeechRecognition
import pyttsx3 # pip install pyttsx3
import datetime # pip install datetime
import pyaudio # pip install pyaudio
import os # pip install os
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser

recognizer = sr.Recognizer() # initialize the recognizer
engine = pyttsx3.init() # initialize the engine


def listen(): # listens to the user's voice and returns the text
    with sr.Microphone() as source: # use the default microphone as the audio source
        print("I'm listening")
        recognizer.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = recognizer.listen(source) # listen for the first phrase and extract it into audio data

        try: # recognize speech using Google Speech Recognition
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
            return text
        except Exception as e: # speech is unintelligible
            print("Apologies, I didn't quite get that")
            return "" # return an empty string if the speech is unintelligible


def speak(text): # text is the text that the assistant will speak
    engine.say(text) # queue up the text to be spoken
    engine.runAndWait() # speak the queued text


def run_assistant(): # main function to run the assistant
    text = listen()
    if "hello Travis" in text:
        speak("Hello there, how can I help you?")
    
    elif "time" in text: # if the user said "time"
        time = datetime.datetime.now().strftime("%H:%M") # get the current time
        speak(f"The current time is {time}")
    
    elif "date" in text: # if the user said "date"
        date = datetime.datetime.now().strftime("%Y/%m/%d") # get the current date
        speak(f"Today's date is {date}")
    
    elif "search" in text: # if the user said "search"
        speak("What would you like to search for?")
        search = listen() # listen to the user's response
        url = f"https://www.google.com/search?q={search}" # generate the search URL
        webbrowser.get().open(url) # open the search URL in the default browser
        speak(f"Here is what I found for {search} on the web") # speak the search results
    
    elif "Wikipedia" in text: # if the user said "Wikipedia"
        speak("Searching Wikipedia")
        text = text.replace("Wikipedia", "") # remove "Wikipedia" from the text
        results = wikipedia.summary(text, sentences=3) # get the summary from Wikipedia
        speak("According to Wikipedia")
        speak(results) # speak the summary
    
    elif "exit" in text:
        speak("Goodbye")
        exit()
    
    else:
        speak("I'm sorry, I'm currently under development and can't help you with that yet")


if __name__ == "__main__": # run the assistant
    while True:
        run_assistant()

# Run the program and say "hello Travis" to start the conversation with the assistant

        