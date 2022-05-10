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

def test_sqlite_threading():
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(p), 0x19, None)


    libname = ctypes.util.find_library(ctypes.util.gdbize(a))
    fn = ctypes.CDLL(libname)
    fn.sqlite3_thread_cleanup()

    try:
        py_threading.start_new_thread(test_sqlite_threading, ())
    except:
        raise

    for i in range(100):
        print(c.execute('select test(1, 2);').fetchall())

    time.sleep(3)
</code>


A:

The crash is occurring on the following line in <code>./Modules/_sqlite/connection.c</code>:
<code>conn_threadid = PyThread_get_thread_ident();
</code>
The problem is that this function uses the <code>Py_single_input</code> variable, which is used by the Python-level <code
