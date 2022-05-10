import ctypes
# Test ctypes.CField
import ctypes
import unittest
from test import support
from ctypes import *

class CFieldTestCase(unittest.TestCase):

    def test_field_sizeof(self):
        # Issue #7: ctypes.sizeof(ctypes.CField) should be 0
        self.assertEqual(sizeof(CField), 0)
        self.assertEqual(sizeof(CField()), 0)

    def test_field_offsetof(self):
        # Issue #7: ctypes.offsetof(ctypes.CField) should be 0
        self.assertEqual(offsetof(CField), 0)
        self.assertEqual(offsetof(CField()), 0)

    def test_field_from_address(self):
        # Issue #7: ctypes.from_address(ctypes.CField) should be None
        self.assertIs(from_address(CField), None)
        self.assertIs(from_address(CField()), None)

class CFieldInStructTestCase(unittest.TestCase):


