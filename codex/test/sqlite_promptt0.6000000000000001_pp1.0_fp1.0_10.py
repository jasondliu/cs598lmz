import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class MyThread(threading.Thread):
    def __init__(self, db, mutex):
        threading.Thread.__init__(self)
        self.db = db
        self.mutex = mutex
        self.stopped = False

    def run(self):
        while not self.stopped:
            self.mutex.acquire()
