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
lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
lib.sqlite3_open_v2.restype = ctypes.c_int

lib.sqlite3_config(ctypes.c_int(9), my_cb, None)

conn = sqlite3.connect(DB_URI, uri=True)

# this works
print(conn.execute("SELECT test(?, ?)", (1, 2)).fetchone()[0])

# this does not
print(conn.execute("SELECT test(?, ?)", (1, 2)).fetchone()[0])

# and this neither
print(conn.execute("SELECT test(?, ?)", (1, 2)).fetchone()[0])
</code>
The error is:
<code>1
Traceback (
