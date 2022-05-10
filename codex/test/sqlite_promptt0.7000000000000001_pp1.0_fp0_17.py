import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("data.sqlite3")

# Create a test database
#db = sqlite3.connect("test.sqlite3")
#cursor = db.cursor()
#cursor.execute("CREATE TABLE base_table (id INTEGER PRIMARY KEY, name TEXT)")
#cursor.execute("CREATE UNIQUE INDEX base_table_name ON base_table (name)")
#cursor.execute("INSERT INTO base_table (name) VALUES (?)", ("Test",))
#db.commit()

# Load the sqlite3 library
sqlite3_path = ctypes.util.find_library("sqlite3")
if not sqlite3_path:
    raise ImportError("Unable to find the sqlite3 library")
sqlite3 = ctypes.CDLL(sqlite3_path)

# Declare sqlite3_open in Python
sqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3.sqlite3
