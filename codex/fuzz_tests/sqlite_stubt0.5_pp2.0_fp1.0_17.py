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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.handle), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_URI, None)
my_threading_local.handle.contents.pAppData = ctypes.c_void_p(id(my_threading_local))
sqlite3.sqlite3_set_authorizer(my_threading_local.handle, my_cb, 0)

my_threading_local.a.execute("select test(1, 2)")
</code>
The above code causes the following error:
<code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 140737246665472 and this is thread id 140737246665472
</code>
The error doesn't occur if I remove the <code>sqlite3.sqlite3_set_authorizer(my_threading_local.handle, my_cb
