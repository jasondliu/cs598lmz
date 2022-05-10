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

lib_name = ctypes.util.find_library("pythonsqlite")

print(lib_name)

dll = ctypes.CDLL(lib_name)
dll.sqlite3_progress_handler.argtypes = (ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
dll.sqlite3_progress_handler.restype = ctypes.c_int

dll.sqlite3_progress_handler(100, None, my_cb, None)

# Do something that keeps db open a while
my_threading_local.a.execute("SELECT test(?);", "hello")

# Then do...

del my_threading_local
