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

def my_fn(a, b):
    return a

if __name__ == "__main__":
    dso = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    dso.sqlite3_auto_extension.restype = None
    dso.sqlite3_auto_extension.argtypes = (ctypes.c_void_p,)

    my_cb_ptr = ctypes.PYFUNCTYPE(ctypes.c_int)(my_cb)

    # Initialize the sqlite extension system
    dso.sqlite3_auto_extension(my_cb_ptr)

    # SQLite MUST be the first to load
    assert (dso.sqlite3_libversion_number < my_fn(my_fn(1, 2), 3))

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.create_function("test", 2, my_fn)

    conn.execute("select test(?, ?)", (
