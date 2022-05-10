import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# SQLITE3_OPEN_FULLMUTEX	0x0001
# Open with the full mutexes. This is the default.
# SQLITE3_OPEN_READONLY       0x0002
# Open the database for read only access.
# SQLITE3_OPEN_READWRITE	0x0004
# Open the database for reading and writing.
# SQLITE3_OPEN_CREATE	0x0008
# Create and open a new database.

class DB():
    def __init__(self, name):
        self.conn = None
        self.db_name = name
        self.opened = False

    def open(self):
        if self.opened is True:
            print("Error: Database is already opened!")
            return

        print("db.py: Opening %s" % self.db_name)
        self.conn = sqlite3.connect(self.db_name)
        self.opened = True

    def close(self):
        if self.opened is False:
            print("Error: Database is already closed!")
