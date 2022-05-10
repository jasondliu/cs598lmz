import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

lib = ctypes.util.find_library('sqlite3')
if lib is None:
    raise ImportError("Can't find the sqlite3 library!")
sqlite3 = ctypes.CDLL(lib)

print(sqlite3.sqlite3_threadsafe())

try:
    sqlite3.sqlite3_enable_shared_cache(1)
except AttributeError:
    sqlite3.sqlite3_enable_shared_cache = None
    print('No shared cache')
else:
    print('shared cache')

THREADS = 3

class MyThread (threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print ("Thread " + self.name + " starting.")
        # Get lock to synchronize threads
        #threadLock.acquire()
        thread_func()
        # Free lock to release next thread
