import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from time import sleep
from random import randint
from os import system
from keyboard import is_pressed

from termcolor import colored
from colorama import init
init()

def clear():
    system('cls')

def get_color():
    return randint(30, 37)

def get_background():
    return randint(40, 47)

def get_char():
    return chr(randint(33, 126))

def get_color_background():
    return [get_color(), get_background()]

def get_color_background_char():
    return [get_color(), get_background(), get_char()]

def print_color_background_char(color, background, char):
    print(colored(char, color, 'on_' + str(background)), end='')

def print_color_background(color, background):
    print(colored(' ', color, 'on_' + str(background)), end='')

