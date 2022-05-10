import ctypes
ctypes.windll.user32.LockWorkStation()

on_windows = True
cmd = 'rundll32.exe user32.dll,LockWorkStation'

if os.name != 'nt':
    #on_windows = False
    cmd = "gnome-screensaver-command -l"
os.system(cmd)
import win32com.client
sh = win32com.client.Dispatch('WScript.Shell')


sh.SendKeys('{LWIN}', 0)

import pyautogui
pyautogui.press('win')


import pyautogui
pyautogui.click(15, 15)
pyautogui.hotkey('win', 'l')
pyautogui.hotkey('win')
import time
time.sleep(2)

import pyautogui
pyautogui.hotkey('win', 'l')
import pyautogui
pyautogui.hotkey('win')
pyautogui.press('l')

import pyautogui
pyautogui.hotkey('winleft', 'd')
