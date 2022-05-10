import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:")

class TestConnectionObject(object):

    def setup_class(self):
        self.con = sqlite3.connect(":memory:")

    def teardown_class(self):
        self.con.close()
        del self.con

    def test_connection_factory(self):
        """
        Tests sqlite3.Connection.__init__
        """
        cur = self.con.cursor()
        cur.execute("select 42")
        assert cur.fetchone()[0] == 42


class TestAPISqlFunctions(object):
    """
    Tests sqlite module API functions, i.e. those that are not
    methods of the Connection object.
    """

    def setup_class(self):
        self.con = sqlite3.connect(":memory:")

    def teardown_class(self):
        self.con.close()
        del self.con

    def test_apisql_register_adapter(self):
        """
        tests sqlite.register_adapter()
        """
