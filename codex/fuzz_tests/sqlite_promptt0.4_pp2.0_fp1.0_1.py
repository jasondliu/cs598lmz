import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

# http://code.activestate.com/recipes/576684-simple-threading-decorator/
def synchronized(lock):
    """ Synchronization decorator. """
    def wrapper(f):
        def new_function(*args, **kw):
            lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                lock.release()
        return new_function
    return wrapper

class SharedDict(dict):
    def __init__(self, *args, **kwargs):
        super(SharedDict, self).__init__(*args, **kwargs)
        self.lock = threading.RLock()

    def __getitem__(self, key):
        self.lock.acquire()
        try:
            return super(SharedDict, self).__getitem__(key)
        finally:
            self.lock.release()

    def __setitem__(self, key, value):
        self.lock.acquire()
        try:
