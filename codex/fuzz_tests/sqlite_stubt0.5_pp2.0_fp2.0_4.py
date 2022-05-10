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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.a), 1 | 0x20, None)
sqlite3.sqlite3_enable_load_extension(my_threading_local.a, 1)

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_auto_extension(my_cb)

my_threading_local.a.execute("SELECT test(1, 2)")

sqlite3.sqlite3_shutdown()
</code>
This program crashes with:
<code>Fatal Python error: PyThreadState_Get: no current thread

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)
</code>
The issue seems to be that the <code>sqlite3_auto_extension</code> callback is called from a different thread than the one that the connection is created in.

