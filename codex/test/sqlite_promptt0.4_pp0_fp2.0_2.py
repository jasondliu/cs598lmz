import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_authorizer

class TestConnectionSetAuthorizer(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.execute("create table test(x)")

    def tearDown(self):
        self.con.close()

    def CheckAuthorizer(self, action_code, error_message):
        def authorizer_callback(action_code, c1, c2, c3, c4):
            self.assertEqual(action_code, error_message)
            return sqlite3.SQLITE_OK
        self.con.set_authorizer(authorizer_callback)
        self.con.execute("insert into test(x) values (?)", (42,))
        self.con.set_authorizer(None)

    def test_authorizer(self):
        self.CheckAuthorizer(sqlite3.SQLITE_INSERT, "INSERT")
        self.CheckAuthorizer(sqlite3.SQLITE_UPDATE, "UPDATE")
