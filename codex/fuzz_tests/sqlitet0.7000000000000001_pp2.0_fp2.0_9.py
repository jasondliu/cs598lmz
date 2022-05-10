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


def my_cb_del(p):
    a = my_threading_local.a
    del my_threading_local.a
    print("before...")
    a.close()
    print("after...")
    return 1


sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb_del)

sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_shutdown()
</code>
Output is:
<code>before...
Traceback (most recent call last):

