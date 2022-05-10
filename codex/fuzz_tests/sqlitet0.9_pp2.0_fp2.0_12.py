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

test_cb = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p(0)))
lib.sqlite3_blob_open(ctypes.c_void_p(0), ctypes.c_void_p(0), ctypes.c_void_p(0), ctypes.c_void_p(0), ctypes.c_void_p(0), ctypes.c_void_p(0), test_cb)
</code>
It seems to be not predictable which thread will start the garbage collector. If it is the thread from which I started the code, everything seems to work. If it is another thread, the <code>__del__</code> in the <code>sqlite3.Connection</code> will be called and the garbage collector may try to do some work, which will crash since the callback already finished.

