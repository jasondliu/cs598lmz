import ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
"""

# import pyautogui as pag
import win32api
import win32con
import win32gui
# import win32process
import pywintypes
import sys
import os
import time
import datetime
import re

from common.common_functions import *
from common.common_para import *



class Main():
    def __init__(self):
        self.name = 'switch'

    def run(self):

        hwnd_foreground = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd_foreground)
        print(title)

        # hwnd_foreground = win32gui.GetForegroundWindow()
        # print(hwnd_foreground)
        # print(win32gui.GetClassName(hwnd_foreground))
        # print(win32gui.GetWindowText(hwnd_foreground))
        #
        # hw
