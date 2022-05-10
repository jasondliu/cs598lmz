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

def my_cb_dealloc(p):
    my_threading_local.a.close()

    return 0

if __name__ == "__main__":
    # Create an sqlite threading initializer.
    sqlite3.sqlite_initialize()

    # Create our custom SQLite initialization code.
    sqlite3.sqlite3_auto_extension(ctypes.cast(ctypes.byref(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)), ctypes.c_void_p).value)
    sqlite3.sqlite3_auto_extension(ctypes.cast(ctypes.byref(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb_dealloc)), ctypes.c_void_p).value)

    # Run custom initialization code.
    sqlite3.sqlite3_initialize()

    # Create DB connection.
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.executescript("create table test(id)")
