import ctypes
import ctypes.util
import threading
import sqlite3

class Task(threading.Thread):
    def __init__(self, callback, args=()):
        self._callback = callback
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._callback(*self._args)

class SocketTask(threading.Thread):
    def __init__(self, callback, args=(), callback_args=()):
        self._callback = callback
        self._args = args
        self._callback_args = callback_args
        threading.Thread.__init__(self)

    def run(self):
        self._callback(*self._args, *self._callback_args)

class NanoLogger(object):
    def __init__(self, logfile):
        self.logfile = logfile

    def __call__(self, *args):
        with open(self.logfile, 'a') as f:
            f.write(' '.join(map(str,args)) + '\n')

class NanoDB(object):
    def __init__(
