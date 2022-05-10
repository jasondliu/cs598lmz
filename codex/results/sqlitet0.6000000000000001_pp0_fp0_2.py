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

sqlite3.sqlite3_open = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p))(my_cb)

def test_repr_with_open_connection():
    a = sqlite3.connect(DB_URI)
    assert repr(a) == "&lt;sqlite3.Connection object at 0x%x&gt;" % id(a)

def test_repr_with_closed_connection():
    a = sqlite3.connect(DB_URI)
    a.close()
    assert repr(a) == "&lt;sqlite3.Connection object at 0x%x&gt;" % id(a)

def test_repr_with_open_cursor():
    a = sqlite3.connect(DB_URI)
    b = a.cursor()
    assert repr(b) == "&lt;sqlite3.Cursor object at 0x%x&gt;" % id(b)

def test
