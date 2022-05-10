import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect(':memory:')
# Test sqlite3.Cursor
cursor = db.cursor()
# Test sqlite3.execute
cursor.execute("select sqlite_version()")
# Test sqlite3.fetchone
data = cursor.fetchone()
# Test sqlite3.close
db.close()

# Test ctypes.cdll.LoadLibrary
cdll.LoadLibrary(ctypes.util.find_library("c"))

# Test threading.Thread
thread = threading.Thread()
thread.start()
thread.join()
