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
    my_threading_local.a.execute("SELECT test(1, 2)")

    return 1

def my_cb3(p):
    my_threading_local.a.close()

    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

    p = ctypes.c_void_p()

    lib.sqlite3_open(ctypes.c_char_p(DB_URI), ctypes.pointer(p))

    lib.sqlite3_create_function_v2(p, ctypes.c_char_p(b"test"), 2, 1, None, my_cb, None, None, None)

    lib.sqlite3_exec(p, ctypes.c_char_p(b"SELECT test(1, 2)"), my_cb2, None, None)

    lib.sqlite3_
