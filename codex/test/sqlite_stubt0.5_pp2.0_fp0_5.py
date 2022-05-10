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

def my_cb3(p):
    raise sqlite3.OperationalError("test")

def my_cb4(p):
    raise SystemError("test")

def my_cb5(p):
    raise TypeError("test")

def my_cb6(p):
    raise MemoryError("test")

def my_cb7(p):
    raise ValueError("test")

def my_cb8(p):
    raise RuntimeError("test")

def my_cb9(p):
    raise Exception("test")

def my_cb10(p):
    return 0

def my_cb11(p):
    return 2

def my_cb12(p):
    return "test"

def my_cb13(p):
    return "test", "test2"

def my_cb14(p):
    return "test", "test2", "test3"

