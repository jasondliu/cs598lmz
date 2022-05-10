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

    return 1, p

assert isinstance(sqlite3.Cursor, ctypes.Array)
assert isinstance(sqlite3.Connection, ctypes.Array)

sqlite3.enable_callback_tracebacks(True)
sqlite3.register_adapter(sqlite3.Cursor, lambda cur: cur.fetchall())
sqlite3.register_adapter(sqlite3.Connection, lambda con: 42)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
open = lib.sqlite3_open_v2
open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
close = lib.sqlite3_close_v2
close.argtypes = [ctypes.c_void_p]
create_function = lib.sqlite3_create_function_v2
create_function.argtypes = [ctypes.c_void_p, ctypes.c_char_p, c
