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

    return 1, 1

sqlite3.enable_callback_tracebacks(True)
sqlite3.sqlite_set_authorizer(my_cb, 1)
conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.close()
my_threading_local.a = None
threading.Thread(target=lambda: None).start().join()
</code>
Observed behaviour:
<code># valgrind --log-file=valgrind.log --leak-check=full python3 run.py 2&gt;&amp;1
ERROR:sqlite3:connection garbage collected before connection was closed.
</code>


A:

If you run your program a second time, you don't observe the leaking state any more, do you?
You must understand that the Python garbage collector is not designed to reclaim circular references immediately. Your circular reference is tricky to uncover because the memory allocator may use different allocations for the same address.
To try to reclaim circular references in a callback, you should use the event mechanism (see <code>enable_callback_events</
