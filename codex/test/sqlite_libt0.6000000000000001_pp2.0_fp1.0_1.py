import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import Queue

from ctypes import *
from ctypes.wintypes import *

from lib.commonlib import *

class PYHOOK(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.data_queue = Queue.Queue()
        self.create_db()
        self.start_thread()
        self.init_hook()

    def init_hook(self):
        self.lib = ctypes.windll.LoadLibrary(r'lib\pyhook.dll')
        self.kbHook = self.lib.kbHook
        self.kbHook.argtypes = [c_int, c_int, c_int, c_int]
        self.kbHook.restype = c_int
        self.kbHook.errcheck = self.errcheck
        self.kbHook(2, 0, 0, 0)
        self.kbHook.errcheck = None

