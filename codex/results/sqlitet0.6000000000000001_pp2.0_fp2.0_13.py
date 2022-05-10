import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def my_cb2(p):
    del my_threading_local.a
    return 1

class SQLiteThreadingTests(unittest.TestCase):

    def setUp(self):
        sqlite3.enable_callback_tracebacks(True)
        self.db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def tearDown(self):
        self.db.close()
        del self.db

    def CheckThreading(self):
        # sqlite3_threadsafe() returns 1, 2 or 3.
        threadsafe = sqlite3.sqlite_version_info >= (3, 6, 5)
        if sqlite3.sqlite_version_info >= (3, 7, 4):
            threadsafe = sqlite3.sqlite_version_info >= (3, 7, 6)
        if sqlite3.sqlite_version_info >= (3, 8, 0):
            threadsafe = sqlite3.sqlite_version_info >= (3, 8, 11)
       
