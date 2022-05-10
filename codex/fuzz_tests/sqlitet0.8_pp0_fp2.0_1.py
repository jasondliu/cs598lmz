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

def my_cb_2(z, x):
    my_threading_local.a.execute("select test(?)", (x,))
    return 0

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("pthread"))
    lib.pthread_key_create.argtypes = (ctypes.c_void_p, ctypes.c_void_p)

    c_p = ctypes.c_void_p()
    lib.pthread_key_create(ctypes.byref(c_p), my_cb)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 1, my_cb_2)
    conn.execute("select test(?)", (1,))

main()
