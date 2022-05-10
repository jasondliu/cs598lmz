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

    return 15

class UDF(ctypes.c_int):
    @staticmethod
    def execute():
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("libsqlite3"))
        lib.sqlite3_create_function_v2
        lib.sqlite3_create_function_v2.restype = sqlite3.Connection
        lib.sqlite3_create_function_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        global my_cb
        a = lib.sqlite3_create_function_v2(None, "my_cb", 1, 0, None, my_cb, None, None)
        my_cb = a

def main():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_
