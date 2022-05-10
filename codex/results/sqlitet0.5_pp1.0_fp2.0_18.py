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

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(3, my_cb, 0)
    conn = sqlite3.connect(DB_URI, uri=True)
    conn.execute("create table t (x)")
    conn.execute("insert into t values (test(?, ?))", (1, 2))
    conn.execute("select * from t")

main()
</code>
The above code crashes when the <code>conn.execute</code> call is made.  The crash is caused by the Python interpreter trying to call the <code>test</code> function from the <code>my_threading_local.a</code> object, which has already been deleted by the time the call is made.
If I add a <code>print</code> statement before the <code>conn.execute</code> call, it works perfectly.  It also works if I move the <code>conn</code> object into the <code>my_threading_local</code> object, and then
