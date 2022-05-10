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

def main():
    #  This is a very simplistic and minimalist example of how to use the
    #  SQLite connection object.
    #  It is not meant to be a complete example. In particular, it doesn't:
    #   - properly handle errors
    #   - process the result
    #   - use column names
    #   - protect against SQL injection

    sqlite3.sqlite3_initialize()
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

    sql_conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    p = ctypes.c_void_p(0)
    sqlite3.sqlite3_prepare_v2(sql_conn._conn, b"SELECT test(2, 3)", -1, p, 0)

    sqlite3.sqlite3_exec(sql_conn._conn, b"SELECT test(2, 3)", my_cb, None, 0)

    t1 = threading.Thread(target=sql
