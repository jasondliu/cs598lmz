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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(1, 1)
    lib.sqlite3_initialize()

    lib.sqlite3_create_function_v2(None, "my_cb", 1, 0, None, my_cb, None, None, None)
    lib.sqlite3_create_function_v2(None, "my_cb2", 1, 0, None, my_cb2, None, None, None)

    t = threading.Thread(target=lambda: lib.sqlite3_create_function_v2(None, "my_cb", 1, 0, None, my_cb, None, None, None))
    t.start()
    t.join()

    conn = sqlite3.connect(DB_URI, uri=True)
   
