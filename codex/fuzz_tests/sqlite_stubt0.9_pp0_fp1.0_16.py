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

sqlite3.sqlite3_trace_v2(my_cb)
print "initialized"
for i in xrange(1000):
    print "i", i
    con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    for j in xrange(100):
        cur = con.execute("select test(?, ?)", (j, ))
        assert cur.fetchone()[0] == j
    con.close()
    if i % 10 == 0:
        print "did", i
print "done"
