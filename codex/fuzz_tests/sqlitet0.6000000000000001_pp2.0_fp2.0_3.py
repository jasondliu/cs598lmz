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

sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db_con))
sqlite3.sqlite3_enable_load_extension(my_threading_local.db_con, 1)
sqlite3.sqlite3_load_extension(my_threading_local.db_con, ctypes.util.find_library("sqlite3"), "sqlite3_my_cb", ctypes.c_void_p(ctypes.addressof(my_cb)))

print(my_threading_local.a.execute("select test(1, 2)").fetchall())
</code>
I'm using a custom <code>Connection</code> class, so that I can override <code>__del__</code> and make sure that the connection is closed.

