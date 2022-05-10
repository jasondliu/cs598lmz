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


def main():
    sqlite3.enable_shared_cache(False)
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db),
                            sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE |
                            sqlite3.SQLITE_OPEN_URI, ctypes.c_char_p(None))

    sqlite3.sqlite3_create_collation(my_threading_local.db, b"my_collation", None, my_cb)

    my_threading_local.db.reconnect()

    with my_threading_local.a as a:
        a.execute("select test(1, 2)")

main()
del my_threading_local.a
