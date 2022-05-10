import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# Test sqlite3.execute
# Test sqlite3.execute_batch
# Test sqlite3.executemany
# Test sqlite3.executescript
# Test sqlite3.row_factory
# Test sqlite3.PARSE_DECLTYPES
# Test sqlite3.PARSE_COLNAMES

MEMORY_ONLY = ':memory:'

class SQLite3Test(unittest.TestCase):
    """This is a test case for sqlite3."""

    def setUp(self):
        self.db = sqlite3.connect(MEMORY_ONLY)

    def tearDown(self):
        self.db.close()

    def test_connect(self):
        # Test sqlite3.connect.
        self.db.close()
        db = sqlite3.connect(MEMORY_ONLY, uri=True)
        self.assertEqual(db.connection, db.execute('select 1').connection)

    def test_execute(self):
        # Test sqlite3.execute.
        cursor
