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

def my_cb2(p):
    a = my_threading_local.a
    del my_threading_local.a

    return 1

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))

sqlite3.sqlite3_create_function_v2(my_threading_local.db,
                                   "my_cb", 0, None,
                                   (1).__class__,
                                   None,
                                   ctypes.cast(my_cb,ctypes.c_void_p),
                                   None, None)

sqlite3.sqlite3_create_function_v2(my_threading_local.db,
                                   "my_cb2", 0, None,
                                   (1).__class__,
                                   None,
                                   ctypes.cast(my_cb2,ctypes.c_void_p),
                                   None, None)

c = my_threading_local.db

for x in range(100):
   
