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
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_initialize()

    lib.sqlite3_config(lib.SQLITE_CONFIG_LOG, my_cb, 0)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = conn.cursor()
    cur.execute("select test(?, ?)", (1, 2))

    print(cur.fetchone())
    print(my_threading_local.a)

    # This is the important part

    del my_threading_local.a

    # This is the important part

    cur.execute("select test(?, ?)", (1, 2))
    print(cur.fetchone())

if __name__ == "__main__":
    main()
</code>

