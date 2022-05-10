import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()
try:
    conn = sqlite3.connect(':memory:')
    conn.close()
except:
    print('Error: sqlite3.connect()')

# Test sqlite3.Cursor().execute()
