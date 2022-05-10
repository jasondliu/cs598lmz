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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite_initialize()

sqlite3.sqlite_set_authorizer(my_cb, 0)

conn = sqlite3.connect(DB_URI, uri=True)

conn.close()

print("ok")
