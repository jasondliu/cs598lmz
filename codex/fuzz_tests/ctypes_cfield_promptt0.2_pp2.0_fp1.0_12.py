import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTest(unittest.TestCase):

    def test_field_sizeof(self):
        # Issue #15897: ctypes.sizeof(ctypes.CField) should return 0.
        self.assertEqual(ctypes.sizeof(ctypes.CField), 0)

    def test_field_offsetof(self):
        # Issue #15897: ctypes.offsetof(ctypes.CField) should return 0.
        self.assertEqual(ctypes.offsetof(ctypes.CField), 0)

    def test_field_sizeof_offsetof_in_class(self):
        # Issue #15897: ctypes.sizeof(ctypes.CField) and
        # ctypes.offsetof(ctypes.CField) should return 0 even when used in a
        # class.
        class TestClass(ctypes.Structure):
            _fields_ = [
                ("field1", ctypes.CField),
                ("field2", ctypes.CField),
