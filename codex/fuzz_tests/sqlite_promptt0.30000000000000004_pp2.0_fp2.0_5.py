import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

class TestConnection(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")

    def tearDown(self):
        self.con.close()

    def CheckPragma(self, con):
        cur = con.cursor()
        cur.execute("pragma table_info('sqlite_master')")
        self.assertEqual(cur.fetchall(),
                         [
            (0, u'type', u'text', 0, None, 0),
            (1, u'name', u'text', 0, None, 0),
            (2, u'tbl_name', u'text', 0, None, 0),
            (3, u'rootpage', u'integer', 0, None, 0),
            (4, u'sql', u'text', 0, None, 0),
            ])

    def CheckPragmaThread(self, con):
        cur = con.cursor()
        cur.execute("pragma table_
