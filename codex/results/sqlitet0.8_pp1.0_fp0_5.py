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
    if hasattr(my_threading_local, 'a'):
        del my_threading_local.a

    return 1

def my_cb3(p):
    return 1

def my_cb_err(p):
    try:
        a = 1 / 0
    except:
        return 1

def my_cb_mem(p):
    test_fn = ctypes.pythonapi.PyMem_Malloc
    test_fn.restype = ctypes.c_voidp
    test_fn(0)
    return 1

def my_cb_bind(p):
    if my_threading_local.a.connection is not None:
        raise AssertionError()

    my_threading_local.a.execute("select test(1, 2)")

    return 1

def my_cb_bind_err(p):
    my_threading_local.a.execute("select test(1, 2)")

def my_cb_close(p):
    if my_threading
