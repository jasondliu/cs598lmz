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

def my_cb_2(p):
    a = my_threading_local.a
    a.close()

    return 1

if __name__ == '__main__':
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_config(lib.SQLITE_CONFIG_SERIALIZED)

    lib.sqlite3_initialize()

    lib.sqlite3_test_control(lib.SQLITE_TESTCTRL_EXPLAIN_STMT, my_cb)
    lib.sqlite3_test_control(lib.SQLITE_TESTCTRL_EXPLAIN_STMT, my_cb_2)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    conn.execute("select test(1, 2)")

    lib.sqlite3_shutdown()
