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

try:
    sqlite3.enable_shared_cache(True)
except:
    pass

sqlite3.sqlite3_config(ctypes.c_int(7), ctypes.c_void_p(0))
sqlite3.sqlite3_soft_heap_limit64(400000000000000000000)
sqlite3.sqlite3_config(ctypes.c_int(2), ctypes.c_void_p(my_cb))
sqlite3.sqlite3_soft_heap_limit64(400000000000000000000)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

