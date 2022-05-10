import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    conn = sqlite3.connect('test.db')
except:
    print('Could not connect to sqlite3')

# Test ctypes.util
libc = ctypes.CDLL(ctypes.util.find_library('c'))
# Test threading.Timer
try:
    threading.Timer(1.0, lambda: None)
except:
    print('Could not threading.Timer')
