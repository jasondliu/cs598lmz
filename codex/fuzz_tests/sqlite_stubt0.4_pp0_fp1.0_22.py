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

sqlite3.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db))

sqlite3.sqlite3_commit_hook(my_threading_local.db, my_cb, None)

sqlite3.sqlite3_exec(my_threading_local.db, "begin", None, None, None)

sqlite3.sqlite3_exec(my_threading_local.db, "commit", None, None, None)

print(my_threading_local.a)

sqlite3.sqlite3_close(my_threading_local.db)
</code>
The output is:
<code>&lt;__main__.deleting_conn object at 0x7f9c8b8d3c10&gt;
</code>
The problem is that the <code>deleting_conn</code> object is not deleted. If I comment out the <code>sqlite3.sqlite3_close(my_threading_local.
