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

def cb_wrapper(*args):
    fn = args[0]
    return fn(*args[1:])

# Loading the SQLite shared library. "sqlite3" is an alias for the shared
# library and will be used by Python (at runtime) to load the library.
sqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)

a = sqlite3.sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.pointer(ctypes.c_voidp(0)), 2 | 4 | 32, None)

sqlite3.sqlite3_key(a, 'test'.encode('utf-8'), 4)

s = sqlite3.sqlite3_prepare_v2(a, "CREATE TABLE test (col1, col2);".encode('utf-8'), 256, ctypes.pointer(ctypes.c_voidp(0)), None)

sqlite3.sqlite3_step(s)

sqlite3.sql
