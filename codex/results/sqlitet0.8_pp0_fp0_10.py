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
lib.sqlite3_config(ctypes.c_int(0x201), my_cb)
lib.sqlite3_initialize()

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("create table test(one integer, two text, three text)")

print('finished')
</code>
The output does contain the print statement, but none of the functions are registered, and therefore any attempt to use it will fail.


A:

You have to use <code>sqlite3_config</code> with one of the following options:

<code>SQLITE_FILE_OPEN</code>
<code>SQLITE_OPEN</code>
<code>SQLITE_OPEN_MAIN_DB</code>

<code>SQLITE_FILE_OPEN</code> is the only one that Python's SQLite implementation uses.

