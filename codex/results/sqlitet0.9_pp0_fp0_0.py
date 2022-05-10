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

c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
lib = ctypes.util.find_library('c')
c_func = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

call_back_fn = ctypes.CDLL(lib).sqlite3_commit_hook
call_back_fn(c._sqlite3.connection, c_func, 0)

c.commit()

del c

import gc
gc.collect()

my_threading_local.a.execute("select test(1, 2)")
</code>

