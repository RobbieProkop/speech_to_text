import speech_recognition as sr

r = sr.Recognizer()

def record_audio():
  with sr.Microphone() as source:
    audio = r.listen(source)
    voice_data = ""
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      print('Sorry, I did not understand that')
    except sr.RequestError:
      print("Apologies, my speech service is down")
  
    return voice_data

print("How can I help you?")
voice_data = record_audio()

    
  
  
  