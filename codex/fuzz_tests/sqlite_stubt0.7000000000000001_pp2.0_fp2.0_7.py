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

def my_cb2():
    my_threading_local.a.close()

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    c_cb2 = ctypes.CFUNCTYPE(None)(my_cb2)

    lib.sqlite3_enable_load_extension(1)
    lib.sqlite3_extension_init(0,0,0)
    lib.sqlite3_auto_extension(c_cb2)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, my_cb)

    for i in range(100):
        conn.execute("SELECT test(2, 3)")
        conn.cursor().execute("SELECT test(2, 3)")
        conn.execute("SELECT test(?, ?)
