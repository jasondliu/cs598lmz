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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p()))

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open(DB_URI.encode(), ctypes.byref(ctypes.c_void_p()))
</code>
This fails with:
<code>sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 1112 and this is thread id 1720
</code>
I'm assuming this is because I'm creating the sqlite connection in <code>my_cb</code> and then trying to use it in <code>test_fn</code> which is being called by <code>ctypes</code> which is in a different thread.
I would like to know if there is anyway I can make this work? Is it possible to trick <code>sqlite3</code> into thinking that the thread which
