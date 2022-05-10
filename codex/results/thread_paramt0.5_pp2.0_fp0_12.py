import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b]2;title\x07")).start()

from pynput import keyboard
import time
from pyautogui import *

# start winamp
#os.system("C:\Program Files (x86)\Winamp\winamp.exe")

# start spotify
#os.system("C:\Users\joshu\AppData\Roaming\Spotify\Spotify.exe")

# start chrome
#os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

# start vscode
#os.system("C:\Users\joshu\AppData\Local\Programs\Microsoft VS Code\Code.exe")

# start sublime
#os.system("C:\Program Files\Sublime Text 3\sublime_text.exe")

# start notepad
#os.system("C:\Windows\System32\notepad.exe")

# start calculator
#os.system("C:\Windows\System32\calc.exe")

# start cmd
#os.system("C:\
