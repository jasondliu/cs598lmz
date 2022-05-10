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

    return 10

sqlite3.sqlite3_config(SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_uri_boolean(DB_URI, "a", 1)
sqlite3.sqlite3_uri_boolean(DB_URI, "b", 0)
sqlite3.sqlite3_uri_int64(DB_URI, "c", 0)
sqlite3.sqlite3_uri_int64(DB_URI, "d", -1)

b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
b.row_factory = sqlite3.Row
b.execute("create table test (a int, b int)")
b.execute("insert into test (a, b) values (?, ?)", (1, 2))
b.execute("insert into test (a, b) values (?, ?)", (3, 4))
b.execute("insert into test (a, b) values (?, ?)", (5, 6))
b.execute("insert into test (a, b) values (?, ?)", (
