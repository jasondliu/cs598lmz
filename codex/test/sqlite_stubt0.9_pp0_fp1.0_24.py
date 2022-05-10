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

p = ctypes.POINTER(ctypes.c_int)()
p1 = ctypes.cast(ctypes.byref(p), ctypes.c_void_p)
print(ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open(DB_URI.encode(), ctypes.byref(p1)))
print(ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_db_config(p, 3, my_cb))


print(ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_close(p))
print(ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open(DB_URI.encode(), ctypes.byref(p1)))

