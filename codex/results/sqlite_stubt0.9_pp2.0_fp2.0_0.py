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

def bad_cb(p):
    return "a"

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(109, my_cb)
lib.sqlite3_config(13, bad_cb)


def f():
    conn = sqlite3.connect(DB_URI, uri=True)
    print(conn.execute("select test(1, 2)").fetchall())

a = threading.Thread(target=f)
a.start()
a.join()

f()

b = threading.Thread(target=f)
b.start()
b.join()

c = threading.Thread(target=f)
c.start()
c.join()
</code>

