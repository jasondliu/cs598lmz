import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
db = sqlite3.connect(":memory:")
db.cursor().execute("select * from sqlite_master")

# Test ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

# Test threading.Thread
def test():
    pass
threading.Thread(target=test).start()
