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

def my_open(filename):
    filename = filename.decode()
    if not filename.startswith('file:'):
        return sqlite3.connect(filename)
    else:
        return sqlite3.connect(filename, uri=True)

sqlite3.register_converter("my_open", my_open)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.atexit.restype = ctypes.c_int
libc.atexit(my_cb)

a = sqlite3.connect(DB_URI, uri=True, converter={'a': 'my_open'})
a.execute("CREATE TABLE x (a);")
a.commit()

c = my_threading_local.a.cursor()

c.execute("INSERT INTO x VALUES (test(2, 3))")
# test_fn should raise an error
c.execute("SELECT a FROM x")
</code>
Running the above with <code>python3 segfault.py</
