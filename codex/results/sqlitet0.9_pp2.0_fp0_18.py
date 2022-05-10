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

initialize_sqlite()
sqlite_bindings_init(my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("CREATE TABLE data(what INTEGER)")
newRef = getattr(a, my_refname)

th = threading.Thread(target=thread_target, args=(newRef,))
th.start()
th.join()
</code>

