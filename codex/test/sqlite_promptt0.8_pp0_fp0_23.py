import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
sqlite3.connect(':memory:')
# Test ctypes.find_library()
ctypes.find_library('bz2')
# Test ctypes.CDLL()
# XXX: Is there a better test case for this?
ctypes.CDLL('libc.so.6')
# Test threading.Thread()
threading.Thread(target=lambda: None)
