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
    b = my_threading_local.a

    cursor = b.cursor()
    cursor.execute("select test(1, 2)")
    cursor.close()

    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    p = lib.sqlite3_prepare_v2(0, "select 1", -1, 0, 0)

    lib.sqlite3_preupdate_hook(p, my_cb, 0)
    lib.sqlite3_preupdate_hook(p, my_cb_2, 0)

    lib.sqlite3_step(p)
    lib.sqlite3_finalize(p)

if __name__ == "__main__":
    main()
</code>

