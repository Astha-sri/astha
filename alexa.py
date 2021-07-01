import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import wikipedia
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
       pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
 
    
    elif  'tell me about' in command:
        talk('crazibrain solution is a private company.Mr.Nishchaya Dave is founder of crazibrain solution, it was incorporated in 16 november 2018, pioneers in Gamification, mobile apps, AR/VR, making and executing campaigns,and Mobile marketing.its moto is To create the perfect blend of technology and creativity for the best business solution')
    elif 'members are there'in command:
        talk('there are total 16 members in crazibrain solution.')
    elif 'join new member' in command:
        talk('total of five  members joined crazibrain solution this year.')
    elif'clients of'in command:
        talk('there are numerous of  clients in crazibrain solution such as cleartrip,britania,etc')
    

    
    elif 'joke' in command:
        talk(pyjokes.get_joke())  
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)         
    elif 'who is the' or'what is'or 'where' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)   
      


    else:
        talk('Please say the command again.')    




while True:
    run_alexa() 