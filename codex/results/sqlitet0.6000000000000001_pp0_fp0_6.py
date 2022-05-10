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

def my_cb2(a):
    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

class MyThread(threading.Thread):
    def run(self):
        libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        libsqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
        libsqlite3.sqlite3_open_v2.restype = ctypes.c_int

        class OpenStruct(ctypes.Structure):
            pass

        p_open = ctypes.POINTER(OpenStruct)()

        ret = libsqlite3.sqlite3_open_v2(":memory:", ctypes.byref(p_open), 0x00000001 | 0
