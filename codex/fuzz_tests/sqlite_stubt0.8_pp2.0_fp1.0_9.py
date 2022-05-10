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

sqlite3.register_adapter(my_threading_local, my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
with a:
    a.execute("CREATE TABLE test (value)")
    a.execute("INSERT INTO test VALUES (test(?, ?))",
              (my_threading_local, u"test"))
    assert a.execute("SELECT value FROM test").fetchone()[0] == u"test"
</code>
I find it incredibly useful to adapt a threading_local() object to a sqlite connection when I need one disposing bound to the connection. I would like to know if this is safe at all.
I am also thinking of a way to have a per-thread cache of sqlite connections using a threading.local(), but I am not sure if this is a bad idea. Is there anything obvious I am missing?

