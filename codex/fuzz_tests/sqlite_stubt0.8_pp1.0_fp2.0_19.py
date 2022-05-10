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

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

sqlite3.enable_callback_tracebacks(True)

with sqlite3.connect(DB_URI, isolation_level=None) as conn:
    conn.create_function("test_callback", 1, cb)
    conn.execute("select test_callback(0)")
    conn.execute("select test(1, 2)")
</code>
If I run it through the flamegraph visualization script on Linux, it looks like it's biting me at the <code>_sqlite3.so</code> level:

If I toggle the ephemeral mode off, however, the problem goes away:
<code>DB_URI = "test"
</code>

What is creating such a large number of database connections in the ephemeral mode case?  How can I avoid it?

