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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.conn),
    sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)

my_threading_local.conn.dbapi.create_function("my_cb", 1, my_cb)

my_threading_local.conn.dbapi.execute("select my_cb(?);", (1, ))

my_threading_local.conn.dbapi.execute("select test(?, ?);", (1, 2))

my_threading_local.a.execute("select test(?, ?);", (1, 2))

# This should work, because the Connection is still alive.
del my_threading_local.a

# But this should fail, because the Connection is now dead.
my_threading_local.conn.dbapi.execute("select test(?, ?);", (1, 2))
</code
