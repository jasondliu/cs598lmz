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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_set_authorizer(None, my_cb)

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
cur = conn.cursor()
cur.execute("select test(1, 2)")
result = cur.fetchone()[0]
del cur
del conn

for i in range(10):
    q = Queue()
    t = Thread(target=my_threading_local.a.execute, args=("select test(1, 2)",), kwargs={"fetchall": q})
    t.start()
    t.join()
    assert q.get()[0][0] == result
