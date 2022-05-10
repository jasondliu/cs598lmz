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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.conn), 0x00000002, None)
lib.sqlite3_exec(my_threading_local.conn, b"create table a(b)", None, None, None)
lib.sqlite3_exec(my_threading_local.conn, b"select test(1, 2)", my_cb, None, None)
</code>
This results in a segfault.  If I remove the <code>create_function</code> call, the segfault goes away.  If I add an explicit <code>close</code> call on the connection, the segfault goes away.  If I change the <code>factory</code> to a class that doesn't override <code>__del__</code>, the segfault goes away.
The segfault appears to be occurring when the connection is closed.  If I change the <code>dele
