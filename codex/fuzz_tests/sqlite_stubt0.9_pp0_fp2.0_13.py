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

SQLITE_STATIC = 0
SQLITE_TRANSIENT = -1

def my_init():
    ctypes.pythonapi.PyEval_InitThreads()
    ctypes.pythonapi.PyThreadState_Swap()

    sqlite3.sqlite3_initialize()

    ctypes.pythonapi.PyEval_SaveThread()

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(4, my_cb)

def my_gc():
    a = my_threading_local.a
    my_threading_local.a = None

    ctypes.pythonapi.PyEval_ReInitThreads()

    return sqlite3.function_cleanup(a)

a = None

thread = None

class conn:
    def __init__(self):
        self.a = sqlite3.connect(DB_URI, factory=deleting_conn)

def my_thread():
    global a

    a = conn()

    c
