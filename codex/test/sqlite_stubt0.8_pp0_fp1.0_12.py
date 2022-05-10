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

class Test(ctypes.Structure):
    item = ctypes.c_int

def my_callback(x):
    return 1

def test_sqlite_symbols():
    test = Test()

    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(b"/tmp/test", ctypes.byref(test));

    lib.sqlite3_open_v2(
        b"/tmp/test",
        ctypes.byref(test),
        sqlite3.SQLITE_OPEN_READONLY,
        None);

    lib.sqlite3_open_v2(
        b"/tmp/test",
        ctypes.byref(test),
        sqlite3.SQLITE_OPEN_READONLY,
        ctypes.cast(my_callback, ctypes.c_void_p));

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.close()
    conn = sqlite3
