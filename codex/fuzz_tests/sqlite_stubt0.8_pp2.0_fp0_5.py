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

sqlite3.sqlite3_open = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(sqlite3.sqlite3)))(my_cb)

# Test db
a = sqlite3.connect(DB_URI, uri=True)

print(a.execute("SELECT test(1, 2)").fetchone()[0])

# Clears threading local, should close the connection if not already closed
del my_threading_local
