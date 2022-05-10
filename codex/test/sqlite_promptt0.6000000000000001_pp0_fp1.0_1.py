import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.Cursor.execute

# load the sqlite3 library
sqlite3.load_extension('/usr/local/lib/libsqlitefunctions.dylib')

# connect to database
conn = sqlite3.connect('../data/test.db')

# create a cursor
c = conn.cursor()

# create a table
