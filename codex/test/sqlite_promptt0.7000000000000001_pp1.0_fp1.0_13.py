import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection
#import sqlite3.connection

class SqliteDB_shared(object):
    def __init__(self):
        self.db = sqlite3.connect('test.db')
        self.initialized = True

    def get_db(self):
        return self.db

    def close_db(self):
        self.db.close()

class SqliteDB(object):
    def __init__(self):
        #self.db = sqlite3.connect('test.db', check_same_thread = False)
        self.db = sqlite3.connect('test.db')
        self.initialized = True

    def get_db(self):
        return self.db

    def close_db(self):
        self.db.close()


class DbTest(unittest.TestCase):
    def test_thread(self):
        db = SqliteDB()
