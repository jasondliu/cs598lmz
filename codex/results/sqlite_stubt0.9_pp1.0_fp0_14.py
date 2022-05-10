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

def main():
    # TODO memleaks
    d = sqlite3.dllbase
    for sym in dir(d):
        p = getattr(d, sym, None)
        if p and not sym.startswith('_') and sym.startswith('sqlite3'):
            p = ctypes.cast(p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_voidp)))
            p.errcheck = lambda p, fn, args: None

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_config(ctypes.c_int(10), ctypes.c_int(1))
    sqlite3.sqlite3_config(ctypes.c_int(30), ctypes.c_int(1))

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b = sqlite3.connect(DB_URI
