import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import sys
sys.path.append('../')
import config

# Threading
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
