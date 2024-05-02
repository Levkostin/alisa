import speech_recognition as sr
import pyttsx3
import random

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk('пон')
def listen_and_save():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk('Что хотел')
        r.pause_threshold = 1
        r.
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio,language = 'ru-RU').lower()
    except sr.UnknownValueError:
        talk('Не поняла')
        task = listen_and_save()
    return task
a = ['вы мне не нравитесь','я сегодня не разговорчивая','скидка 70 процентов на шампунь от леомакс']
def Make(task):
    if 'привет' in task:
        talk('Пока')
    else:
        b = choice(a)
        talk(b)
    
make(listen_and_save())

