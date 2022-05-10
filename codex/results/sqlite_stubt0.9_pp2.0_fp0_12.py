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

p = None

try:
    p = sqlite3.SQLiteConnection('test')
    p.create_collation("test_coll", my_cb)
    p.commit()
except Exception:
    if p:
        p.close()

c = threading.Thread(target=threading_test.threaded_func, args=(p,))
c.start()
c.join()
