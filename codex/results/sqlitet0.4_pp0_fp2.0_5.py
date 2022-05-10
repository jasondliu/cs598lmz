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

def my_cb2(p):
    a = my_threading_local.a
    a.execute("select test(1, 2)").fetchall()
    return 1

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(1)
    lib.sqlite3_config(1, my_cb)
    lib.sqlite3_config(2, my_cb2)
    lib.sqlite3_config(3, my_cb2)
    lib.sqlite3_config(4, my_cb2)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("select 1").fetchall()

    for i in range(10):
        t = threading.Thread(target=a.execute, args=("select 1",))
        t.start()
        t.join()

if __name__ == "__main__":
    main()
