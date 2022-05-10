import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:memory:?cache=private')
import time
import sys

if sys.version_info[0] == 3:
    from io import StringIO
else:
    from StringIO import StringIO

import _sqlite3

try:
    from test import support
except ImportError:
    from test import test_support as support

def verbose(fn):
    def wrapper(*args, **kwargs):
        if support.verbose:
            print(fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

#------------------------------------------------------------------------------

class _SQLiteTest(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.execute("create table test(i)")
        self.db.execute("insert into test(i) values (0)")
        self.db.commit()
        self.db.row_factory = sqlite3.Row

    def
