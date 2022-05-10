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
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.execute("select test(?, ?)", (1, 2))
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode("utf8"), ctypes.pointer(ctypes.c_voidp()))
lib.sqlite3_create_function(None, b"test", -1, None, None, my_cb, my_cb2, my_cb3)

t1 = threading.Thread(target=lib.sqlite3_create_function, args=(None, b"test", -1, None, None, my_cb, my_cb2, my_cb3))
