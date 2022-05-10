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

def my_step(p):
    if p != None:
        return 1
    else:
        return 0

def my_final(p):
    a = my_threading_local.a

    if a != None:
        a.close()

    return 1

SQLITE_TRANSIENT = -1

def my_bind(a, b, c):
    c = ctypes.cast(c, ctypes.POINTER(ctypes.c_int))
    c[0] = len(b)

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.a))

sqlite3.sqlite3_create_function(my_threading_local.a, "my_cb", 0, 0, 4096, my_cb, my_step, my_final)

sqlite3.sqlite3_prepare_v2(my_threading_local.a, "select my_cb()", -1, ctypes.byref(my_threading_local.db_stmt
