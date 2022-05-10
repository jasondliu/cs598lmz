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

def main():
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
    lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(1))

    db = lib.sqlite3_open_v2(ctypes.c_char_p(DB_URI.encode('utf-8')), ctypes.byref(ctypes.c_void_p()), ctypes.c_int(1), ctypes.c_char_p(None))
    assert db == 0

    lib.sqlite3_db_config(ctypes.c_void_p(), ctypes.c_int(10), ctypes.c_int(1), ctypes.c_void_p())
