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

    a = None
    my_threading_local.a = a

    return 1

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

libc.setenv.restype = ctypes.c_int
libc.setenv.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)

libc.setenv("SQLITE_USE_URI", "1")

libc.atexit(my_cb)
libc.atexit(my_cb2)
</code>
This program crashes when calling <code>sqlite3.connect()</code>, but not otherwise. It seems like the second <code>atexit</code> call somehow causes <code>sqlite3.connect</code> to crash. I have a feeling that this is a bug in sqlite3, but I want to make sure that the way I use it is correct first.

