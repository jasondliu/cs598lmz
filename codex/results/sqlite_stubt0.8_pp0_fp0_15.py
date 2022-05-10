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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).\
    sqlite3_initialize()

ctypes.CDLL(ctypes.util.find_library("sqlite3")).\
    sqlite3_db_config(
        ctypes.c_void_p(),
        ctypes.c_int(1001),
        ctypes.c_void_p(
            ctypes.CFUNCTYPE(ctypes.c_int)(
                my_cb)))()
</code>
And then it crashes with:
<code>Fatal Python error: GC object already tracked
</code>
I am fairly certain it's caused by the <code>sqlite3.Connection</code> object being garbage collected after it has been passed as a callback from C back to Python. However, I've tried various different ways to solve it, but none have worked.
I've tried using a global <code>sqlite3.Connection</code> object, and passing the global object to the <code>test_fn</code> function, but it doesn't work (the callback then locks
