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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
LIB_SQLITE3_OPEN = libsqlite3.sqlite3_open
LIB_SQLITE3_OPEN.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p))
LIB_SQLITE3_OPEN.restype = ctypes.c_int

ffi = FFI()
ffi.cdef("""
typedef void (*sqlite3_callback)(void*);
int sqlite3_open(const char *filename, void **ppDb);
""")
C = ffi.dlopen(ctypes.util.find_library("sqlite3"))
C.sqlite3_open(DB_URI, ffi.new("void**"))

conn = sqlite3.connect(DB_URI, uri=True)
conn.create_collation("mycollation", my_cb)

my_threading_local.a.close()
del my_threading_local.
