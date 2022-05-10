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

p = ctypes.c_void_p()
sqlite3.sqlite3_progress_handler(None, my_cb, 1, 0)
# we can't force GC right now as the ctypes call hasn't exited yet so we
# rely on the fact that reducing the interactive prompt's references to
# `p` forces ctypes to deallocate it, calling the handler
p = None

import gc
gc.collect()
print("Now start the interactive prompt")
