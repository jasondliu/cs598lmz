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

    return 100

class Global:
    pass

Global.lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
Global.lib.sqlite3_config(3, my_cb)

a = sqlite3.connect(DB_URI, uri=True)
try:
    a.execute("pragma locking_mode = exclusive")
except sqlite3.Error:
    pass
a.execute("CREATE TABLE t(x)")
a.execute("INSERT INTO t VALUES (?)", (123,))
a.execute("PRAGMA locking_mode")
a.execute("SELECT test(x, ?) FROM t", (1.1,))
a.execute("SELECT test(x, ?) FROM t", (1.1,))
a.close()
</code>
This program (without the initial <code>import</code>s) looks like this:
<code>(py35)⚡ ~/dev/test$ python3.5 test.py
&lt;sqlite3.Row object at 0x738b30&gt;
Trace
