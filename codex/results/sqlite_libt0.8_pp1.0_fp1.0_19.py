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

    def start(self):
        print 'Starting history snapshot process'
        self.history_thread = threading.Thread(target=self.history_loop)
        self.history_thread.daemon = True
        self.history_thread.start()

    def stop(self):
        if self.history_thread:
            print 'Stopping history snapshot process'
            self.history_thread.join()
            self.history_thread = None

    def history_loop(self):
        try:
            self.db = self.pywb.db_manager.connect()
            last_size = self.get
