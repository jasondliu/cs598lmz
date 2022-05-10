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

_sqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)

# register our callback
pfn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)

_sqlite.sqlite3_progress_handler.argtypes = (ctypes.c_void_p, ctypes.c_int, pfn, ctypes.c_void_p)

print "[*] Enabled progress hook"

# test our hook
conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("create virtual table test using fts4(tokenize=porter)")
for i in xrange(1000):
    conn.execute("insert into test values(?)", ("test(%s)" % i,))

s = conn.cursor()
s.execute("select * from test where test match 'test'")
print "[*] Completed the query"

# THIS LEAKS
s.execute("select * from test where test
