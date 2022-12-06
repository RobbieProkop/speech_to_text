import speech_recognition as sr
import webbrowser

# tell the time
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
  with sr.Microphone() as source:
    if ask:
      print(ask)
    audio = r.listen(source)
    voice_data = ""
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      print('Sorry, I did not understand that')
    except sr.RequestError:
      print("Apologies, my speech service is down")
  
    return voice_data

def respond(voice_data):
  if "what is your name" in voice_data:
    print("My name is Yulia")
  if 'what time is it' in voice_data:
    print(ctime())
  if 'search' in voice_data:
    search = record_audio("what do you want to search for?")
    # searches brave with the search term
    url = 'https://search.brave.com/search?q=' + search
    # opens a new web browser with the search
    webbrowser.get().open(url)
    print("here is what found for " + search)
    
  # location with google maps
  if 'find location' in voice_data:
    location = record_audio("what is the location?")
    # searches brave with the search term
    url = 'https://google.nl/maps/place/' + location + "/&amp;"
    # opens a new web browser with the search
    webbrowser.get().open(url)
    print('Here is the location of ' + location)

print("How can I help you?")
voice_data = record_audio()
respond(voice_data)


  
  
  