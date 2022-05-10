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

if __name__ == "__main__":
    import sys

    sqlite3.enable_callback_tracebacks(True)
    f = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    f.sqlite3_enable_shared_cache(0)
    f.sqlite3_initialize()
    f.sqlite3_open_v2(":memory:", ctypes.byref(ctypes.c_void_p()), 0x00000600, None)
    f.sqlite3_create_function_v2(my_threading_local.a._sqlite_conn, "test", 2, 0x00000800, None, my_cb, None, None, None)
    f.sqlite3_close(my_threading_local.a._sqlite_conn)
    f.sqlite3_shutdown()
    sys.exit(0)
