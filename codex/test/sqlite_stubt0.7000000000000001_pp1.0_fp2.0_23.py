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

if __name__ == "__main__":
    import threading
    sqlite3.connect(":memory:", uri=True, factory=deleting_conn).close()
    sqlite3.sqlite3_open_v2(":memory:", ctypes.pointer(ctypes.c_void_p()), 0, None)
    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.sqlite3_config(1)
    sqlite3.sqlite3_enable_load_extension(1)
    sqlite3.sqlite3_load_extension(ctypes.util.find_library("sqlite3"), "sqlite3_my_cb", None)

    def fn():
        sqlite3.connect(DB_URI, uri=True).execute("select test(1, 2)").fetchall()
        conn = sqlite3.connect(":memory:", uri=True)
        conn.execute("select test(1, 2)").fetchall()
