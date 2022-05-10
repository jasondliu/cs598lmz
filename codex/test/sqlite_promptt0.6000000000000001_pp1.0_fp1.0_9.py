import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# connection = sqlite3.connect(':memory:')
# connection.close()
# Test ctypes
try:
    # ctypes.cdll.LoadLibrary('libc.so.6')
    ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
except OSError:
    pass
else:
    raise Exception('Expected OSError')
# Test threading
threading.Thread(target=lambda: None)
