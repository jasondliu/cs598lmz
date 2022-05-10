import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import pyautogui
pyautogui.click(1542, 889) # click on coordinates
pyautogui.typewrite('Hello world!', interval=0.2) # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')

import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
pyperclip.paste()

import time
print(time.time())  # current timestamp in seconds since epoch (1/1/1970)
print(time.localtime())  # current time in struct_time format
print(time.asctime())  # current time in string format
print(time.ctime())  # current time in string format
