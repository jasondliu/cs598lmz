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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_create_function(None, b"test_fn", 1, 0, None)
lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(my_threading_local.a), 0, None)
lib.sqlite3_start_backup(
    my_threading_local.a,
    ctypes.c_char_p(b'main'),
    ctypes.c_char_p(b'main'),
    0,
    ctypes.cast(
        ctypes.cast(
            ctypes.cast(
                ctypes.py_object(my_cb),
                ctypes.c_void_p
            ),
            ctypes.POINTER(ctypes.c_void_p)
        ),
        ctypes.POINTER(ctypes.c_int)
    )
)
</code>
The code above segfaults.
This is what valgrind reports:
<
