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
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
    lib.sqlite3_enable_shared_cache(1)

    lib.sqlite3_extension_init()

    lib.sqlite3_config(2, my_cb, None)

    con = sqlite3.connect(DB_URI, uri=True)
    cur = con.cursor()
    cur.execute("select test(1, 2)")

    con = sqlite3.connect(DB_URI, uri=True)
    cur = con.cursor()
    cur.execute("select test(1, 2)")

    a = my_threading_local.a
    del a

if __name__ == "__main__":
    main()
