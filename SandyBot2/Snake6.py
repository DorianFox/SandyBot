import os
import random
import pyttsx3
import eel


@eel.expose
def reply_hello():
    return "world"


eel.init("web")

eel.start("main.html", size=(800, 800))



# all below you can remove

engine = pyttsx3.init()

names = ['Привет', 'о вресии', 'ты кто?', 'О вресии', 'help', 'помощь', 'Помощь', 'привет', '']
print('Привет, чем могу помочь?')
engine.say("Привет, чем могу помочь?")
engine.runAndWait()
appName = input('Чем помочь? \n')

while appName not in names:
    appName = print('Не понимаю о чём ты говоришь.')
    engine.say("Не понимаю о чём ты говоришь.")
    engine.runAndWait()
    print('Затрудняетесь? Введите команду help \n')
    engine.say("Затрудняетесь? Введите команду help")
    engine.runAndWait()
    appName = input('Чем помочь? \n')

if appName == 'ты кто?':
    print('Я Сэнди, говорящая змея)')
    engine.say("Я Сэнди, говорящая змея.")
    engine.runAndWait()
    engine.say("А как тебя зовут? \n")
    engine.runAndWait()
    name = input("А как тебя зовут? \n")
    print("Привет, " + name + "! Рада знакомству!")
    engine.say("Привет, " + name + "! Рада знакомству!")
    engine.runAndWait()