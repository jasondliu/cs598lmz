import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os, time

from pygame import mixer
mixer.init()
mixer.music.load('beep-07.wav')

import pyautogui

pyautogui.FAILSAFE = False

def get_screen_size():
    return pyautogui.size()

def move_mouse_to(x, y):
    pyautogui.moveTo(x, y, duration=0.25)

def move_mouse_to_center():
    x, y = get_screen_size()
    move_mouse_to(x/2, y/2)

def click():
    pyautogui.click()

def click_in_the_middle():
    x, y = get_screen_size()
    pyautogui.click(x/2, y/2)

def double_click():
    pyautogui.doubleClick()

def double_click_in_the_middle():
    x, y = get_screen_size()

