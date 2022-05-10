import ctypes
import ctypes.util
import threading
import sqlite3
import time
from collections import defaultdict

class HISTORY_STATUS(ctypes.Structure):
    _fields_ = [('size', ctypes.c_uint32),
                ('count', ctypes.c_uint32),
                ('version', ctypes.c_uint32)]

class History(object):

    def __init__(self, pywb):
        self.pywb = pywb
        self.db = None
        self.history_thread = None

