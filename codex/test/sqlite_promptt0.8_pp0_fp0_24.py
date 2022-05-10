import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() takes a 'timeout' argument.

libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

class Test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.failure = None

    def run(self):
        try:
            c = sqlite3.connect(":memory:", timeout=0.1)
            c.execute("select 1")
        except Exception as e:
            self.failure = e
        libsqlite.sqlite3_interrup
