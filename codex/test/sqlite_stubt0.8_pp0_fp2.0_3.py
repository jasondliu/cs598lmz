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
    try:
        my_threading_local.a
    except AttributeError:
        print("a is not defined")
    else:
        print("a is defined")
    return 1

def my_cb3(p):
    try:
        my_threading_local.a
    except AttributeError:
        print("a is not defined")
    else:
        print("a is defined")
    return 1

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.create_function("my_cb", 0, my_cb)
db.create_function("my_cb2", 0, my_cb2)
db.create_function("my_cb3", 0, my_cb3)

sqlite3_exec = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3')).sqlite3_exec

sqlite3_exec.argtypes = ctypes.c_void_p, ctypes.c_
