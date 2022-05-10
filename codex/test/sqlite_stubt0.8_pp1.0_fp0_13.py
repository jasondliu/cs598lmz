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

libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
sqlite3.sqlite3_extension_init = libsqlite3.sqlite3_extension_init
sqlite3.sqlite3_extension_init.argtypes = (
    ctypes.c_int,
    ctypes.py_object,
    ctypes.py_object,
    ctypes.py_object,
)
sqlite3.sqlite3_extension_init.restype = ctypes.c_int

sqlite3.sqlite3_extension_init(0, None, my_cb, None)

if __name__ == "__main__":
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    for i in range(100000):
        a.execute("SELECT test(1, 2);")

    del a
