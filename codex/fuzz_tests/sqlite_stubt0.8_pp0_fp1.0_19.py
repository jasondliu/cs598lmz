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

ctypes.CDLL(ctypes.util.find_library("pysqlcipher"))

pysqlcipher.sqlcipher_init.argtypes = [ctypes.py_object]
pysqlcipher.sqlcipher_init.restype = ctypes.c_int

ret = pysqlcipher.sqlcipher_init(my_cb)
print("sqlcipher_init returned: %d" % ret)

conn = my_threading_local.a
c = conn.cursor()

print("pysqlcipher version: %d" % pysqlcipher.PYSQLCIPHER_VERSION)
print("sqlite version: %s" % c.execute("select sqlite_version()").fetchone()[0])

c.execute("select test(1, 2)")
print("result: %s" % c.fetchone()[0])

print("sqlite source id: %s" % c.execute("select sqlite_source_id()").fetchone()[0])

c.execute
