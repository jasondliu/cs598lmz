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

lib.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))

lib.sqlite3_update_hook(my_threading_local.db, ctypes.cast(my_cb, ctypes.c_void_p), 0)

lib.sqlite3_exec(my_threading_local.db, b"create table test(a, b);", 0, 0, 0)

lib.sqlite3_exec(my_threading_local.db, b"insert into test values(1, 2);", 0, 0, 0)

lib.sqlite3_close(my_threading_local.db)
</code>
I get an error when the <code>deleting_conn</code> object is deleted:
<code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140735776715136 and this
