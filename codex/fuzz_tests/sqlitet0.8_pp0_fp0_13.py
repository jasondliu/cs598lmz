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

def my_cb_a(p):
    cur = my_threading_local.a.cursor()
    cur.execute("select test(?)", (1,))
    cur.close()
    return 1

def my_cb_dealloc(p):
    my_threading_local.a.close()
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("pthread"))

    cb = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb), ctypes.c_void_p).value
    cb_a = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb_a), ctypes.c_void_p).value
    cb_dealloc = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb_dealloc), ctypes.c_void_p).value

    lib.test_in_thread(cb, cb_a,
