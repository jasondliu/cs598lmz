import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

from pynput.keyboard import Key, Listener
import time
import pyautogui

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.f1:
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')
        pyautogui.hotkey('ctrl','win','left')


    elif key == Key.f2:
       
