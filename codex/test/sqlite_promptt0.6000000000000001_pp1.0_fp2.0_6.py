import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.create_function
#
# This test is based on the test_function_overloading.py test that
# was added to the sqlite3 test suite at 3.4.2.
#
# The original test was modified to use a few more types and to
# create the functions and test them in the same thread.  The
# original test used two threads, one to create the functions and
# another to test them.  This caused problems on Windows.
#
class TestCreateFunction:

    def setup_method(self, method):
        self.con = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()

    def teardown_method(self, method):
        self.cur.close()
        self.con.close()

    def test_buffer(self):
        def x(b):
            return '%s (%s)' % (b, type(b))
        self.cur.execute("select 1")
