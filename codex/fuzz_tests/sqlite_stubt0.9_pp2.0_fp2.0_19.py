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

cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
lib = ctypes.CDLL(ctypes.util.find_library('test'))
lib.test_open_with_callbacks(ctypes.c_int(0), cb_type(my_cb), None)

with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
    my_threading_local.a.close()
    del my_threading_local.a
    conn.execute("select test(x) from generate_series(0, 10) as g(x)")
</code>
This produces the following backtrace.  Notice that the connection is not in the threading local once the error occurs:
<code>Traceback (most recent call last):
  File "test.py", line 28, in &lt;module&gt;
    conn.execute("select test(x) from generate_series(0, 10) as g(x)")
OperationalError:
