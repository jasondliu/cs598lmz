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

sqlite3.enable_callback_tracebacks(True)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(1)

cb = ctypes.SQLITE_TRACE_STMT(my_cb)
lib.sqlite3_trace_v2(0, 4, cb, 0)

c = sqlite3.connect(DB_URI)
c.execute("select test(?);", (1,))
try:
    c.execute("select test(?);", (1,))
except sqlite3.OperationalError:
    pass
</code>


A:

You are not supposed to create threads in sqlite callbacks.
The documentation explicitly says that opening a new database connection or reentering the SQLite library from another thread will result in undefined behavior.
In particular, you mustn't create a thread from within an sqlite callback.

