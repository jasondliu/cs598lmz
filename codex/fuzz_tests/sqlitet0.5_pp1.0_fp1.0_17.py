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

sqlite3.sqlite3_initialize()

p = ctypes.c_void_p()
sqlite3.sqlite3_open(DB_URI, ctypes.byref(p))

sqlite3.sqlite3_create_function(p, "myfunc", 1, 0, ctypes.cast(my_cb, ctypes.c_void_p))

for i in range(0, 100):
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("select myfunc(1)")
    conn.close()

sqlite3.sqlite3_close(p)
sqlite3.sqlite3_shutdown()
</code>
The above code, when run on Python 3.5.1, will crash with a segfault.
The following code, however, does not crash:
<code>import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):

