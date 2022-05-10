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
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]

a = lib.sqlite3_open("test", None)
print("a", a)
lib.sqlite3_set_authorizer(a, my_cb, 0)
lib.sqlite3_close(a)

del a

print("my_threading_local.a", my_threading_local.a)
print("my_threading_local.a.total_changes", my_threading_local.a.total_changes)

del my_threading_local.a
