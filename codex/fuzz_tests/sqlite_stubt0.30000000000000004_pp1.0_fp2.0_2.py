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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
lib.sqlite3_config(ctypes.c_int(7), ctypes.c_void_p(ctypes.cast(ctypes.pythonapi.PyCapsule_New.restype(ctypes.c_void_p)(my_cb, None, None), ctypes.c_void_p)))

a = sqlite3.connect(DB_URI, uri=True)

print(a.execute("select test(1, 2)").fetchall())

del my_threading_local.a

print(a.execute("select test(1, 2)").fetchall())
</code>

