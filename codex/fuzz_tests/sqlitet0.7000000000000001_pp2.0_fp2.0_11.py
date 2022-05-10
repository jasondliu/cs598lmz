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
    sqlite3.load_extension("./pysqlite_test.so")

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.set_progress_handler(my_cb, 100)
    a.execute("create table test(x integer)")

    a.execute("insert into test(x) values (1)")

    a.execute("select test(x, 1) from test")
    a.execute("select test(x, 1) from test")

    del a

    import gc
    gc.collect()

    for i in range(100):
        print("collect")
        gc.collect()
