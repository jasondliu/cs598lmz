import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.create_aggregate with multiple threads.
#
# For python 2.5 and earlier, this test passes if it does not crash.
# For python 2.6 and later, this test passes if it does not crash or
# fail an assertion.

# This test is not intended to be run on its own.  It is run by test_sqlite3.py.

try:
    from test.test_sqlite3 import have_threads
except ImportError:
    have_threads = True


if have_threads and hasattr(sqlite3, 'threadsafety'):
    sqlite3.threadsafety
    sqlite3.threadsafety > 0
else:
    have_threads = False

class ThreadTests(unittest.TestCase):
    database = 'test.db'

    def setUp(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(x)')
