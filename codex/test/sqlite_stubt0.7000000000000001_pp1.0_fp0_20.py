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

# The callback here is a no-op, except that it stores the connection in a
# thread local variable.  In real life, this callback would do something
# interesting with the connection.

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open_v2("file::memory:?mode=memory", ctypes.byref(p), 0x0004 | 0x0200, None)
lib.sqlite3_open("", ctypes.byref(p))

lib.sqlite3_db_config(p, 0x0003, 1, ctypes.byref(cb))

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

lib.sqlite3_db_config(p, 0x0003, 1, ctypes.byref(cb))

lib.sqlite3_close(p)

