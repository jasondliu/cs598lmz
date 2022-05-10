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

lib = ctypes.cdll.LoadLibrary( ctypes.util.find_library('sqlite3') )
lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(5))
if lib.sqlite3_enable_shared_cache(ctypes.c_int(1)):
    raise Exception("sqlite3_enable_shared_cache() failed")

if lib.sqlite3_open_v2(":memory:", ctypes.cast(None, ctypes.POINTER(ctypes.c_void_p)), 4, None):
    raise Exception("sqlite3_open_v2() failed")

lib.sqlite3_db_config(0, ctypes.c_int(8), ctypes.cast(0,ctypes.c_void_p))
lib.sqlite3_db_config(0, ctypes.c_int(26), ctypes.cast(my_cb,ctypes.c_void_p))

lib.sqlite3_close(0)

import sqlite3

conn
