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

def test_open():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    lib.sqlite3_open_v2.restype = ctypes.c_int

    # this is the thing to sqlite3_open_v2
    db = ctypes.c_void_p()
    # open the database
    ret = lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(db), 1, None)
    # configure it
    lib.sqlite3_busy_handler(db, my_cb, None)

    # create a table
    lib.sqlite3_exec(db, "create table foo (a int, b int)", None, None, None)

    # delete it immediately
    lib.sqlite
