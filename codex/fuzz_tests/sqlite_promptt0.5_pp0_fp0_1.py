import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
# Test sqlite3.connect(':memory:')
import os
import sys

# This is used to test the sqlite3.connect(database[, timeout,
# detect_types, isolation_level, check_same_thread, factory, cached_statements,
# uri]) function.
class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        self.con = sqlite3.connect(self.filename)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(id)')

    def tearDown(self):
        self.cur.close()
        self.con.close()
        os.unlink(self.filename)

    def CheckPragma(self, connection):
        cursor = connection.cursor()
        cursor.execute("PRAGMA database_list")
        result = cursor.fetchone()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0],
