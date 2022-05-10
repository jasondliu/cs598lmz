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

def pyfunc(ctx, argc, argv):
    return 1

def main():
    # Setup
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    sqlite3.enable_callback_tracebacks(True)
    lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_URI), 1)
    lib.sqlite3_create_function_v2(ctypes.c_void_p(0), ctypes.c_char_p(b"pyfunc"),
                                   ctypes.c_int(1), ctypes.c_int(lib.SQLITE_UTF8),
                                   ctypes.c_void_p(0), pyfunc,
                                   None, None, None)
    lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_SINGLETHREAD), 1)
    lib.sqlite3_test_control(ctypes.c_int(lib.SQLITE_TESTCTRL_OPTIMIZATIONS),
