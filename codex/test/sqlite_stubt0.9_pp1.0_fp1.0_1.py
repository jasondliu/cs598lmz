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
    

sqlite3.sqlite3_create_function_v2(
    0, 'thread_cb', 2, 5, 0, my_cb, 0, 0, 0)

if __name__ == "__main__":
    db = sqlite3.connect(DB_URI, uri=True)
    c = db.cursor()

    c.execute('create table t(a)')
    c.execute('begin')
    c.execute('insert into t values(thread_cb())')
    c.execute('select test(a, a) from t')
    assert c.fetchone()[0] == 1
    db.__del__()
