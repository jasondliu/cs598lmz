import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

#v2.0.0

#Importing modules
import os, time, sys, math
from math import sqrt
from os import system
from time import sleep

#Defining variables
version = "2.0.0"

#Defining functions
def cls():
    system("clear")
def slowprint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
def slowprint2(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
def slowprint3(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
def slowprint4(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
