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
    c = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    c.sqlite3_config(4, my_cb, 0)
    for i in range(5):
        x = sqlite3.connect(":memory:")
        x.close()
        # This is actually enough to see the issue
        # x.execute("select test(group_concat(name, ','), 'a') from sqlite_master")
    raw_input('wait')
