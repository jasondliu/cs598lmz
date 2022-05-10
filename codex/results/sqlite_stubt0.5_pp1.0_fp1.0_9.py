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

def my_step(p, a, b, c):
    return my_threading_local.a.execute("SELECT test(?, ?)", (a, b)).fetchone()[0]

def my_final(p):
    my_threading_local.a.close()
    return 1

def my_destroy(p):
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.create_function("test", 2, lambda a, b: a)

    sqlite3_aggregate_context = ctypes.c_void_p
    sqlite3_context = ctypes.c_void_p
    sqlite3_int64 = ctypes.c_int64

    sqlite3.sqlite3_create_function.restype = ctypes.c_int
    sqlite3.sqlite3_create_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p, c
