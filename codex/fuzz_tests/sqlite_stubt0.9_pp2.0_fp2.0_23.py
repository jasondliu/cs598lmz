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

def test_init_connections():
    global DB_URI
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    if sqlite3.sqlite_version_info <= (3, 5, 9):
        db_uri = "file:test_libsqlite3?mode=memory&cache=shared"
        conn.execute("PRAGMA cache_size=1")
        conn.commit()
    else:
        db_uri = "file:test_libsqlite3?mode=memory&cache=private"

    conn = sqlite3.connect(db_uri, uri=True, factory=deleting_conn)

    C = conn.cursor()
    C.execute("create table test(x INTEGER)")
    C.executemany("insert into test(x) values (?)",
                  [(i,) for i in (1,2)])
    conn.commit()
    conn.close()

    libsqlite3_so = "libsqlite3.so"

#   
