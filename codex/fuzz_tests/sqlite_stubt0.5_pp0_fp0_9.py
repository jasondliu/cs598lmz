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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_create_function(my_threading_local.db, b"test_fn", 2, 0, None, my_cb, None, None)

my_threading_local.db.close()
my_threading_local.a.execute("select test(1, 2)").fetchall()
</code>
This code should create a connection with a function, which is then called.
However, the code above raises the following exception:
<code>sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 2, and there are 2 supplied.
</code>
I think this has something to do with the fact that the connection is closed, but I don't know why.
I have tried calling <code>sqlite3_reset</code> and <code>sqlite3_clear_bindings</code> before calling <code>sqlite3_close</code>, but it didn't work.
I have also tried
