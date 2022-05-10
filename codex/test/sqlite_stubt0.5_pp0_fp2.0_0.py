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

def test_fn(a, b):
    return a

class Test(unittest.TestCase):
    def test_function(self):
        self.failUnlessEqual(1, sqlite3.sqlite_version_number)
        self.failUnlessEqual(1, sqlite3.sqlite_version_info[0])
        self.failUnlessEqual(2, sqlite3.sqlite_version_info[1])
        self.failUnlessEqual(3, sqlite3.sqlite_version_info[2])

        sqlite3.enable_shared_cache(True)
        self.failUnlessEqual(True, sqlite3.enable_shared_cache())

        self.failUnlessRaises(sqlite3.ProgrammingError, sqlite3.enable_shared_cache, True)

        sqlite3.enable_shared_cache(False)
        self.failUnlessEqual(False, sqlite3.enable_shared_cache())

