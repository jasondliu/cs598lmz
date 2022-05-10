import ctypes
ctypes.windll.user32.LockWorkStation()

import os
import time
from datetime import datetime
from pywinauto import application
from pywinauto import timings
from pywinauto.findwindows import find_window
from pywinauto.findwindows import find_windows
from pywinauto.findwindows import WindowAmbiguousError
from pywinauto.findwindows import WindowNotFoundError
from pywinauto.application import Application
from pywinauto.application import ProcessNotFoundError
from pywinauto.application import findwindows
from pyautogui import typewrite
from pyautogui import hotkey
from pyautogui import press
from pyautogui import click
from pyautogui import moveTo
from pyautogui import moveRel
from pyautogui import dragTo
from pyautogui import dragRel
from pyautogui import mouseDown
from pyautogui import mouseUp
from pyautogui import mouseInfo
from pyautogui import screenInfo
from pyautogui import size
from pyautogui import position
from pyaut
