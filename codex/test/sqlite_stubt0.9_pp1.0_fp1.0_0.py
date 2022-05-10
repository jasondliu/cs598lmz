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

lib = None
if sys.platform.startswith("linux"):
    lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
elif sys.platform.startswith("freebsd"):
    lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
elif sys.platform.startswith("darwin"):
    lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
elif sys.platform.startswith("win"):
    lib = ctypes.CDLL(ctypes.util.find_library("msvcrt"))

my_cb_p = sqlite3.SQLITE_TRANSIENT_INP_FREE
my_cb_fn = sqlite3.SQLITE_TRANSIENT_INP_FREE(my_cb)

lib.system(my_cb_fn)

assert hasattr(my_threading_local, "a")

