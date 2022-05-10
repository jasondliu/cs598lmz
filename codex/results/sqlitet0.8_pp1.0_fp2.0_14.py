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

lib_name = ctypes.util.find_library("sqlite3")
print("Using %r" % (lib_name))

sqlite3 = ctypes.CDLL(lib_name)

sqlite3.sqlite3_config(ctypes.c_int(1), ctypes.c_int(0))
sqlite3.sqlite3_initialize()

i_t = ctypes.c_int
i_p = ctypes.POINTER(i_t)

database = ctypes.c_void_p()

sqlite3.sqlite3_open_v2(b"test",
                        ctypes.POINTER(ctypes.c_void_p)(database),
                        64 | 4,
                        None)

sqlite3.sqlite3_open_v2(b":memory:",
                        ctypes.POINTER(ctypes.c_void_p)(database),
                        64 | 4,
                        None)

if not hasattr(sqlite3, "sqlite3_open_v2"):
    print("sqlite
