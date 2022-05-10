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
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(ctypes.c_int(2), ctypes.c_int(1))

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test", 1, my_cb)
    a.execute("create table test(a, b)")
    a.execute("insert into test values(test(5), test(5))")
    del a

    for i in range(1, 100):
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        a.execute("insert into test values(test(5), test(5))")
        del a

main()
</code>
To run this, you'll need to install <code>libsqlite3-dev</code> or equivalent, and make sure it's on the <code>LD_LIBRARY_PATH</code>. Otherwise the
