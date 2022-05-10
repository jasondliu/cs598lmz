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
    if my_threading_local.a:
        my_threading_local.a.close()

    for conn in deleting_conn.instances:
        conn.close()

    return 0

class HookTC():
    def __init__(self):
        self.dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        self.dll.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)]
        self.dll.sqlite3_create_function_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_
