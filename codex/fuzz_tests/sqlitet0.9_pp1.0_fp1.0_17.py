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


ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite3_trace_v2(None, 0, ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)(my_cb))


# (memory leaks on python 3.2, OSError on python 2.7 on the following line)
sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
