import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file.x1').close()


class Lock(object):

    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()


class RWLock(object):

    def __init__(self):
        self.l = threading.Lock()
        self.rCount = [0]
        self.wcount = [0]

    def acquire_read(self):
      #  if self.wcount[0] > 0: raise IOError('in write operation')
      #  if self.l.locked(): raise IOError('in write operation')
        self.rCount[0] += 1
        if self.rCount[0] == 1: self.l.acquire()

    def release_read(self):
        if self.rCount[0] == 0: raise IOError('not reading')
        self.rCount[0] -= 1
        if self.r
