import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#sqlite3.connect(':memory:')
#sqlite3.connect('test.db')

# Test ctypes.util.find_library()
lib = ctypes.util.find_library('sqlite3')
assert lib

# Test ctypes.cdll.LoadLibrary()
test = ctypes.cdll.LoadLibrary(lib)

# Test sqlite3.connect(':memory:') + threading
assert sqlite3.connect(':memory:')
assert threading.current_thread()

# Test sqlite3.connect('test.db')
assert sqlite3.connect('test.db')
