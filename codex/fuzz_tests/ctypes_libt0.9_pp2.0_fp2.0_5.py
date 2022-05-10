import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('Cool program for matrix')
import numpy as np
import time
import os
import sys
from pynput.keyboard import Key, Controller
clear = lambda: os.system('cls')
keyboard = Controller()

arr = np.array([[' ' for j in range(320)] for i in range(200)])

gap = 0.1

def rand_clr():
    r = np.random.randint(0,256)
    g = np.random.randint(0,256)
    b = np.random.randint(0,256)
    return '\033[38;2;{};{};{}m#\033[38;2;0;0;0m'.format(r,g,b)

interval_const = 10

interval = interval_const

while True:
    keyboard_value = input()
    if keyboard_value == 'r':
        interval = interval_const
    for j in range(200):
        for i in range(320):
            probability =
