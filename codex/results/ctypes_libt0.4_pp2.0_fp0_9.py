import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32api
import win32con

win32api.MessageBox(0, "Your text", "Your title", win32con.MB_ICONINFORMATION)

import os
os.system('notepad')

import subprocess
subprocess.call(['C:\\Windows\\System32\\notepad.exe'])

import webbrowser
webbrowser.open('http://google.com')

import pyautogui
pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!', interval=0.2)
pyautogui.press('enter')

import pyautogui
pyautogui.screenshot('C:\\Users\\User\\Desktop\\screenshot.png')

import pyautogui
pyautogui.locateOnScreen('C:\\Users\\User\\Desktop\\button.png')

import pyautogui
pyautogui.locateCenterOnScreen('C:\\Users\\User
