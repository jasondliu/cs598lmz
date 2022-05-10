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

if __name__ == '__main__':
    dll = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)
    dll.sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))
    dll.sqlite3_initialize()

    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    dll.sqlite3_auto_extension(cb)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("select test(1, 2)")
