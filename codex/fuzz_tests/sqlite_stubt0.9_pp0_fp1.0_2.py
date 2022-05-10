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


lib_sqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib_sqlite3.sqlite3_config(5, 1)

lib_sqlite3.sqlite3_shutdown()

lib_sqlite3.sqlite3_initialize()

fn_p = ctypes.create_function(len(ctypes.c_void_p), 1, my_cb)

lib_sqlite3.sqlite3_db_config(None, 10, 0, fn_p, None)

lib_sqlite3.sqlite3_shutdown()

lib_sqlite3.sqlite3_initialize()
</code>
I wrote the above to make a function which attempts to use <code>sqlite3</code>'s built in <code>create_function()</code> method. The above code works fine, I would be eternally grateful if you can tell me what is going wrong in my library, so i can make a fix (or if its a bug in SQLite then i'll report it). I am rather new
