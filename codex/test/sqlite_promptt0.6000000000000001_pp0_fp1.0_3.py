import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

# For testing
#import time

# For debugging
#import pdb

class CThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.res = None

    def getResult(self):
        return self.res

    def run(self):
        print ('Starting ' + self.name)
        self.res = self.func(*self.args)
        print ('Exiting ' + self.name)

# ==============================
# ========== GLOBALS ===========
# ==============================

# Set this to 1 to enable debug messages
DEBUG = 0

# Set this to 1 to enable verbose debug messages
VERBOSE_DEBUG = 0

# Set this to 1 to enable error messages
ERROR = 0

# Set this to 1 to enable verbose error messages
VERBOSE_ERROR = 0

# Set this to 1 to enable info
