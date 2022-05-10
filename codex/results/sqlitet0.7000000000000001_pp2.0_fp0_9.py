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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

lib.sqlite3_profile.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), ctypes.c_void_p]

lib.sqlite3_profile(None, ctypes.cast(my_cb, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)), None)

conn = sqlite3.connect(DB_URI, uri=True)
conn.execute("create table t (v)")
conn.execute("insert into t values (test(5, 6))")
cur = conn.cursor()
cur.execute("select * from t")
print(cur.fetchall())
conn.close()
del my_threading_local.a
</code>

