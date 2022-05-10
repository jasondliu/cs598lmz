import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect('test.db')
# Test threading
threading.Thread(target=None)
# Test ctypes
ctypes.util.find_library('c')
