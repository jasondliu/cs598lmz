import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

from . import test_base

class TestUtil(test_base.TestBase):
    def test_load_library(self):
        self.assertTrue(ctypes.util.find_library('sqlite3'))
        self.assertTrue(ctypes.util.find_library('sqlite'))

    def test_load_library_fail(self):
        self.assertRaises(OSError, ctypes.util.find_library, 'sqlite3_missing')
        self.assertRaises(OSError, ctypes.util.find_library, 'sqlite_missing')

    def test_load_library_via_ctypes(self):
        self.assertTrue(ctypes.CDLL(ctypes.util.find_library('sqlite3')))
        self.assertTrue(ctypes.CDLL(ctypes.util.find_library('sqlite')))

    def test_load_library_via_ctypes_fail(self):
        self.assertRaises(OSError, ctypes.CDLL, ctypes.util.find
