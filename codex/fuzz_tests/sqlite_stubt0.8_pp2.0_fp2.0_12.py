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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"),
                         use_errno=True)

libsqlite3.sqlite3_open.restype = ctypes.c_int
libsqlite3.sqlite3_open.argtypes = (ctypes.c_char_p, ctypes.c_void_p)

my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

db = libsqlite3.sqlite3_open(DB_URI.encode("utf-8"),
                             ctypes.c_void_p(my_cb_c))

if db == 0:
    print("Could not open database: {}".format(ctypes.get_errno()))
    exit(1)

exit(0)
</code>
output:
<code>Exception ignored in: &lt;module 'threading' from '/usr/lib64/python3.7/threading.py'&gt
