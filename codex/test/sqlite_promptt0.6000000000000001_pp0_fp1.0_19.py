import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
db = sqlite3.connect('test.db')

# Test ctypes.util.find_library()
lib = ctypes.util.find_library('sqlite3')
lib = ctypes.util.find_library('c')

# Test threading.Thread()
threading.Thread()

# Test threading._allocate_lock()
threading._allocate_lock()

# Test os.urandom()
os.urandom(8)
