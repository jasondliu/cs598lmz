import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

class libc(object):
    """
    A wrapper class for the C libc library
    """
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'))

    def get_tid(self):
        """
        Get the thread id of the current thread
        """
        return self.libc.syscall(186)

class Sqlite3(object):
    """
    A wrapper class for the C sqlite3 library
    """
    def __init__(self):
        self.sqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

    def open(self, filename):
        self.filename = filename
        self.db = ctypes.c_void_p()
        ret = self.sqlite3.sqlite3_open(filename.encode('utf-8'), ctypes.byref(self.db))
        if ret:
            raise sqlite3.OperationalError(self
