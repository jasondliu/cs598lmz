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
sqlite3.set_authorizer(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()), 0, None)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 25, in my_cb
    a.create_function("test", 2, test_fn)
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 140383344006656 and this is thread id 140383344006656
</code>
I am using Python 3.6.3 and sqlite3 3.21.0.

