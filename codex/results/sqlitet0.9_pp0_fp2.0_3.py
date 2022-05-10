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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local._handle),
                       sqlite3.SQLITE_OPEN_URI | sqlite3.SQLITE_OPEN_MEMORY,
                       ctypes.c_char_p(ctypes.util.find_library('sqlite3')))

sqlite3.sqlite3_progress(my_threading_local._handle.value, 100, my_cb, 1)

print(my_threading_local.a.execute("select test(?, ?)", (1, 2)).fetchone()[0])
&gt;&gt;&gt; 1
</code>
After running this script using <code>python3.8 -X tracemalloc -m main -u dialog</code> (with Python 3.7 and 3.8), a dialog with the title <code>Program error</code> is shown for both versions, with the message <code>main: Fatal IO error 5 (Input/output error) on X server :0.0.</code>
I know
