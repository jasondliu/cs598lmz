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

def my_cb_none(p):
    return None

def my_cb_null(p):
    return None

def my_cb_int(p):
    return 1

def my_cb_float(p):
    return 1.0

def my_cb_text(p):
    return "test"

def my_cb_blob(p):
    return b"test"

def my_cb_unicode(p):
    return "test"

def my_cb_buffer(p):
    return bytearray(b"test")

def my_cb_memoryview(p):
    return memoryview(b"test")

def my_cb_tuple(p):
    return (1,)

def my_cb_list(p):
    return [1]

def my_cb_generator(p):
    yield 1

def my_cb_wrong_return(p):
    return "test", 1

def my_cb_wrong_arg(p):
    return 1,

def my_
