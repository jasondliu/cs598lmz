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

lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
lib.setenv.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
lib.setenv.restype = ctypes.c_int
lib.setenv("SQLITE_HOOK_INIT", "my_cb", 0)

lib.sqlite3_initialize()

sqlite3.connect(DB_URI, uri=True).execute("select test(1, 2)").fetchall()

lib.sqlite3_shutdown()
</code>

