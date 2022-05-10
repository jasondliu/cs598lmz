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

ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
# sqlite.sqlite3_open_v2 needs a CDLL instance
sqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)

# the callback function that we'll call populate_db
callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

# attach a sqlite3_vfs to execute our callback
attach_threading_local = sqlite.sqlite3_attach_vfs(ctypes.c_char_p(b"attach-threading-local"), callback, 0, 0)

with sqlite3.connect(DB_URI, uri=True) as conn:
    r = conn.execute
