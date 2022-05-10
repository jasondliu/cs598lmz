import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(mmap_size=None).
# The mmap_size=None option causes sqlite3 to leave the mmap file
# size as is. All os.fstat() calls in this file should return the
# same result regardless of whether sqlite3.connect(mmap_size=None)
# is used.

MMAP_SIZE = 1024 * 1024 * 8

def resize(filename, new_filesize):
    dylib = ctypes.util.find_library("c")
    cdll = ctypes.cdll.LoadLibrary(dylib)
    ftruncate = cdll.ftruncate
    ftruncate.argtypes = [ctypes.c_int, ctypes.c_long]
    ftruncate.restype = ctypes.c_int
    return ftruncate(os.open(filename, os.O_RDWR), new_filesize)

class Resizer:
    def __init__(self, db):
        self.db = db

    def start(self):
        t = threading.Thread(target=self.run
