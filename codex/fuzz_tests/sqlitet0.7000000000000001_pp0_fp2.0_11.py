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

ctypes.pythonapi.PyEval_InitThreads()
ctypes.pythonapi.PyEval_ReleaseThread(ctypes.pythonapi.PyEval_SaveThread())

my_cb(None)

a = my_threading_local.a

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

a.create_function("test", -1, test_fn)

def test_fn(a, b):
    return a

a.create_function("test", 1, test_fn)

def test_fn(a, b):
    return a

a.create_function("test", 0, test_fn)

def test_fn(a, b):
    return a

a.create_function("test", -3, test_fn)

def test_fn(a, b):
    return a

a.create_function("test", -2, test_fn)

def test_fn(a, b):
    return a

a
