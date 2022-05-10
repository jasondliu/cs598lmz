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

p = ctypes.POINTER(pysqlite_ext.SQLiteExtension)
assert sqlite3.sqlite_api_routines
sqlite3.sqlite_api_routines.aggregate_context(
    sqlite3.sqlite_api_routines.aggregate_count, 1)
#sqlite3.sqlite_api_routines.set_authorizer(my_cb, p)
#conn = sqlite3.connect(DB_URI, uri=True)
#conn.cursor().execute("select test(1);")
#my_threading_local.a.cursor().execute("select test(1);")
#print my_threading_local.a.iterdump()
#print conn.iterdump()
