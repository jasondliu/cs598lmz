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

sqlite3.sqlite3_set_authorizer(my_cb, None)

conn = sqlite3.connect(DB_URI, uri=True)
</code>
This piece of code crashes with the following error:
<code>*** Error in `python': double free or corruption (!prev): 0x000055b6d43b5f00 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7f9c9f9a97e5]
/lib/x86_64-linux-gnu/libc.so.6(+0x8037a)[0x7f9c9f9b237a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7f9c9f9b5b9c]
/usr/lib/x86_64-linux-gnu/libsqlite3.so.0(sqlite3_free+0x21)[0x7f
