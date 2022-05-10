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

class Test(unittest.TestCase):
    def test_threading(self):
        # Initialize threading
        from sqlite3 import dbapi2 as sqlite
        sqlite.SQLITE_ENTER = 0
        sqlite.SQLITE_LEAVE = 2
        sqlite.SQLITE_CREATE_SUBTYPE = 3
        sqlite.SQLITE_CREATE_COLLATION = 4
        sqlite.SQLITE_CREATE_FUNCTION = 5
        sqlite.SQLITE_CREATE_AGGREGATE = 6
        sqlite.SQLITE_DELETE_COLLATION = 8
        sqlite.SQLITE_DELETE_FUNCTION = 9
        dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

        ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(threading.currentThread().ident),
            ctypes.py_object(SystemError))

        self.assertTrue(dll.sqlite3_config(sqlite.SQL
