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

sqlite3.enable_callback_tracebacks(True)
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
lib.sqlite3_open.restype = ctypes.c_int

conn = ctypes.c_void_p()
lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(conn))

lib.sqlite3_create_function(conn, "test", 1, ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)(my_cb), None, None)
lib.sqlite3_exec(conn, "select test(1)", None, None, None)

lib.sqlite3_close(conn)

del my_threading_local.a
