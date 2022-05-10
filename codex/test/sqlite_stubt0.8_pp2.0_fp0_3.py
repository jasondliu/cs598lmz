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

lib = ctypes.CDLL(ctypes.util.find_library("ltdl"))
lib.lt_dlinit()
lib.lt_dlerror.restype = ctypes.c_char_p

lib.sqlite3_enable_load_extension(None, 1)
lib.sqlite3_load_extension("extension-functions.so", None, ctypes.cast(my_cb, ctypes.c_void_p))
#if lib.sqlite3_load_extension("extension-functions.so", None, ctypes.cast(my_cb, ctypes.c_void_p)) != 0:
#    print lib.sqlite3_errmsg(None)

a = my_threading_local.a

print(a.execute("SELECT test(2, 3)").fetchone()[0])

lib.lt_dlexit()
