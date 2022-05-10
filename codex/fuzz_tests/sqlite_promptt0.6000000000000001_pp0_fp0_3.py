import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/dev/shm/test.db')
# Test sqlite3.connect('file:/dev/shm/test?mode=memory&cache=shared')
# Test sqlite3.connect('file:/dev/shm/test?mode=memory&cache=private')
# Test sqlite3.connect(':memory:')

class test_sqlite3(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')

    def tearDown(self):
        self.db.close()

    def CheckPragma(self, name, expected):
        cur = self.db.execute('PRAGMA %s' % name)
        row = cur.fetchone()
        self.assertEqual(row[0], expected,
                         '%s has unexpected value %s, expected %s' %
                         (name, row[0], expected))

    def CheckPragmaType(self, name, expected):
        cur = self.db.execute('PRAGMA %s' % name)
        row = cur
