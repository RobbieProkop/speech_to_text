import speech_recognition as sr
import webbrowser
import time

# dependencies of playing sound back
import playsound
import os
import random
from gtts import gTTS

# tell the time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
  with sr.Microphone() as source:
    if ask:
      yulia_speak(ask)
    audio = r.listen(source)
    voice_data = ""
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      yulia_speak('Sorry, I did not understand that')
    except sr.RequestError:
      yulia_speak("Apologies, my speech service is down")
  
    return voice_data

def yulia_speak(audio_string):
  tts = gTTS(text=audio_string, lang='en')
  r = random.randint(1, 10000000)
  audio_file = 'audio-' + str(r) +'.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

def respond(voice_data):
  if "what is your name" in voice_data:
    yulia_speak("My name is Yulia")
  if 'what time is it' in voice_data:
    yulia_speak(ctime())
  if 'what date is it' in voice_data:
    yulia_speak(ctime())
  if 'yulia search' in voice_data:
    search = record_audio("what do you want to search for?")
    # searches brave with the search term
    url = 'https://search.brave.com/search?q=' + search
    # opens a new web browser with the search
    webbrowser.get().open(url)
    yulia_speak("here is what found for " + search)
    
  # location with google maps
  if ' yulia find location' in voice_data:
    location = record_audio("what is the location?")
    # searches brave with the search term
    url = 'https://google.nl/maps/place/' + location + "/&amp;"
    # opens a new web browser with the search
    webbrowser.get().open(url)
    yulia_speak('Here is the location of ' + location)
    
  # exit / close the program
  if "exit" in voice_data:
    yulia_speak('Goodbye')
    exit()
# continuouse listening
time.sleep(1)

yulia_speak("How can I help you?")
while 1:
  voice_data = record_audio()
  respond(voice_data)


  
  
  