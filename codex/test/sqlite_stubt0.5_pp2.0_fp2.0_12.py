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

def test_threading():
    # test that a threading local sqlite connection can be used
    # with a custom create_function
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_thread_cleanup()

    lib.sqlite3_open_v2(DB_URI.encode("ascii"), ctypes.byref(my_threading_local.conn),
        sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)

    lib.sqlite3_open(DB_URI.encode("ascii"), ctypes.byref(my_threading_local.conn2))

