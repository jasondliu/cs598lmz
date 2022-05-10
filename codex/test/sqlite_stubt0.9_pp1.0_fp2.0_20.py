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

lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
lib.sigsetjmp.restype = lib.sigsetjmp(None, 0)
err = lib.sigsetjmp(None, 0)

with sqlite3.connect(DB_URI, uri=True) as db:
    db.create_function('testfn', 1, my_cb)

################################################################################
#
# This is issue http://bugs.python.org/issue9171
#
# If you have a threading.local() object, and use it in a pysqlite
# create_function() call, create_function() will create a reference cycle
# involving the threading.local() object, causing memory to be leaked.
#
# This bug is triggered with Python 3.3, and was probably introduced
# between Python 3.3.0 and Python 3.3.1.
#
# It is similar to issue http://bugs.python.org/issue4217.
#
# This issue was discovered when using Werkzeug with Python
