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
    my_threading_local.a.close()

    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    # this loads the sqlite3 lib
    sqlite3.connect(DB_URI, uri=True)

    p = ctypes.util.find_library("sqlite3")
    libsqlite3 = ctypes.CDLL(p)

    libsqlite3.sqlite3_initialize()

    ctypes.pythonapi.PyEval_InitThreads()

    ctypes.pythonapi.PyEval_AcquireThread(ctypes.py_object(threading.current_thread()))

    ctypes.pythonapi.PyThreadState_Swap(ctypes.py_object(my_threading_local).interpreter)

    libsqlite3.sqlite3_set_authorizer(0, my_cb, None)
    libsqlite3.sqlite3_set_authorizer(0, my_cb2, None)

    a = sqlite
