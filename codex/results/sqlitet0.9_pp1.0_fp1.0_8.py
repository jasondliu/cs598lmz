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

def run_t(num_t):
    try:
        libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    except OSError:
        raise SystemExit("ERROR: unable to find sqlite3 library")
    cbfunctype = ctypes.CFUNCTYPE(
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_void_p)
    )

    libsqlite.sqlite3_initialize()
    libsqlite.sqlite3_shutdown.restype = ctypes.c_int
    libsqlite.sqlite3_shutdown.argtypes = ()

    libsqlite.sqlite3_open.restype = ctypes.c_int
    libsqlite.sqlite3_open.argtypes = (
        ctypes.c_char_p,  # const char *filename
        ctypes.POINTER(ctypes.c_void_p),  # sqlite3 **ppDb
    )

    libsqlite.sqlite3_enable
