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

ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open_v2(
    DB_URI.encode(),
    ctypes.byref(my_threading_local.a),
    sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_MEMORY,
    None
)

my_threading_local.a.create_collation("test", my_cb)

my_threading_local.a.execute("SELECT test('a', 'b')")

print("done")
</code>

