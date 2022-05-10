import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') - in-memory database

class sqlite3M(object):
    """
    Wrapper for sqlite3 library.

    """

    # i don't use self
    def __init__(self):
        self.libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
        # Create a connection object to the SQLite database.
        self.db = sqlite3.connect(':memory:')

        self.c = self.db.cursor()
        self.c.execute("""
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            body TEXT
        )
        """)
        self.c.execute("""
        INSERT INTO items (title,body)
        VALUES('I', 'I am initial')
        """)

        self.db.commit() # save changes

        #
        self.db_mutex = threading.RLock() # mutex to lock access to db

        #
