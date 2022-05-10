import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('data.db')

def nl():
    """
    New line
    """
    print()

def get_libc():
    """
    Returns a ctypes interface to libc
    """
    libc_path = ctypes.util.find_library('c')
    return ctypes.CDLL(libc_path)

class GDBInput(threading.Thread):
    """
    Thread used to handle stdin from GDB
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.done = False
        self.line = None

    def run(self):
        self.line = input()
        self.done = True

class GDBOutput(threading.Thread):
    """
    Thread used to handle stdout from GDB
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.done = False
        self.output = None

    def run(self
