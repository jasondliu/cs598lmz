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

# This is required to be called before building the
# connection. Failing to do so will result in an
# assertion error later.
ctypes.CDLL(ctypes.util.find_library('sqlite3')).sqlite3_auto_extension(my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
my_threading_local.a = a

import pdb; pdb.set_trace()

"""
>>> a.execute('select test(1, 2) from sqlite_master').next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ProgrammingError: Could not evaluate function expression: test
"""
