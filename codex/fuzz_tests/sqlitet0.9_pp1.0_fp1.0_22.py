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

lib = ctypes.util.find_library(ctypes.util.find_library("sqlite3"))
if lib is None:
    raise Exception("sqlite library not found")

p = ctypes.CDLL(lib)

if p.sqlite3_open_v2(ctypes.create_string_buffer(DB_URI.encode()), 
    ctypes.byref(ctypes.c_voidp.in_dll(p, "ppDb")), 
    2 | 4, 
    None
) != 0:
    raise Exception("failed to open database")

p.sqlite3_set_authorizer(
    ctypes.c_voidp.in_dll(p, "ppDb").value, 
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
)

if p.sqlite3_close_v2(ctypes.c_voidp.in_dll(p, "ppDb").value) != 0:
    raise Exception("failed to close dat
