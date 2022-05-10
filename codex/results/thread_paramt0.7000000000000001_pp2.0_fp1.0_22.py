import sys, threading
threading.Thread(target=lambda: sys.stdout.write("")).start()

# import pygame for playing sounds
import pygame

# import playsound to play sound
import playsound

# import the random module
import random

# import the sleep module from time
from time import sleep

# import the SpeechRecognition module
import speech_recognition as sr

# import os to join the path of the file
import os

# create an object of SpeechRecognition class
r = sr.Recognizer()

# create a microphone object
mic = sr.Microphone(device_index=0)

# use the microphone object to get the audio
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print("Say Something")
# recognize the speech using google
try:
    print("Text: "+ r.recognize_google(audio))
except:
    pass

# use the microphone object to get the audio
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio
