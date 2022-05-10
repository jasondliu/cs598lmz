import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import pytest

from . import util

class TestConnection(util.TestCase):
    def test_factory(self):
        def factory(x):
            return x
        con = sqlite3.connect(':memory:', factory=factory)
        self.assertEqual(con.__class__, factory)

    def test_timeout(self):
        con = sqlite3.connect(':memory:', timeout=1.0)
        self.assertEqual(con.isolation_level, None)
        self.assertEqual(con.get_autocommit(), 1)
        self.assertEqual(con.in_transaction, 0)
        self.assertEqual(con.total_changes, 0)
        self.assertEqual(con.row_factory, sqlite3.Row)
        self.assertEqual(con.text_factory, str)
        self.assertEqual(con.connection.get_autocommit(), 1)
        self.assertEqual(con.connection.in_trans
