import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect(":memory:")
cursor = db.cursor()
cursor.execute("select sqlite_version()")
print(cursor.fetchone())
db.close()

# Test ctypes.util.find_library
print(ctypes.util.find_library("c"))

# Test threading
print(threading.current_thread())

# Test ctypes
print(ctypes.c_int(1).value)
