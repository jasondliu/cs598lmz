import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
basePath = os.path.dirname(os.path.abspath(__file__))
dbFile = os.path.join(basePath, 'test.db')
print(dbFile)
conn = sqlite3.connect(dbFile)
conn.close()

# Test ctypes.util.find_library
print(ctypes.util.find_library('c'))
