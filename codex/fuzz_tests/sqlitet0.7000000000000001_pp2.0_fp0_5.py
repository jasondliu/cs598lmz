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

if __name__ == "__main__":
    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_config(1, ctypes.cast(my_cb, ctypes.c_void_p), None)
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("test", 2, lambda a, b: a)
    conn.close()
    print("done")
