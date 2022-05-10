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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.a), sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_MEMORY | sqlite3.SQLITE_OPEN_CREATE, None)

my_threading_local.a.create_function("sqlite3_update_hook", 1, my_cb)

my_threading_local.a.execute("DROP TABLE IF EXISTS test_table")
my_threading_local.a.execute("CREATE TABLE test_table (a int)")
my_threading_local.a.commit()
my_threading_local.a.execute("INSERT INTO test_table VALUES (1)")

# Causes segfault
print my_threading_local.a.execute("SELECT test(a,a) FROM test_table").fetchone()
</code>
I guess I'm missing something obvious, but I can't see what.


A:

Calling the <code>
