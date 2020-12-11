import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def start_cmd():
  try:
    with sr.Microphone() as source:
      print('listening...')
      voice = listener.listen(source)
      cmd = listener.recognize_google(voice)
      cmd = cmd.lower()
      if 'alexa' in cmd:
        cmd = cmd.replace('alexa', '')
        print(cmd)

  except:
    pass
  
  return cmd

  def run_zena():
    cmd = start_cmd()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in cmd:
        person = cmd.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in cmd:
        talk('sorry, I have a headache')
    elif 'are you single' in cmd:
        talk('I am in a relationship with bassim my creator')    
    elif 'give me a joke' in cmd:
        talk(pyjokes.get_joke())
    elif 'am i ugly' in cmd:
        talk('yes you are sorry this is the truth')   
         
    else:
        talk('Please say the cmd again.')


while True:
    run_zena()