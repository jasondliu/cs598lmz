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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.a))
libsqlite3.sqlite3_enable_load_extension(my_threading_local.a, 1)
libsqlite3.sqlite3_load_extension(my_threading_local.a, "./test.so", None, ctypes.byref(my_threading_local.b))
libsqlite3.sqlite3_close(my_threading_local.a)

print("ok")
</code>
The <code>test.so</code> is a simple shared library:
<code>#include &lt;sqlite3ext.h&gt;

SQLITE_EXTENSION_INIT1

int sqlite3_extension_init(sqlite3 *db, char **pzErrMsg, const sqlite3_api_routines *pApi)
{
   
