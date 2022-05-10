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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

sqlite3.sqlite3_test_control(0x00000312, get_ipython().user_ns, my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.execute("create table test (a, b)")
a.execute("insert into test values (1, 2)")

print(list(a.execute("select test(a, b) from test")))

a.close()
</code>

