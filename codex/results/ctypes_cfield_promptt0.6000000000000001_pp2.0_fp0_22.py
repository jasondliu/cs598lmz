import ctypes
# Test ctypes.CField.
import ctypes
import unittest
from test import support
CTYPE = ctypes._SimpleCData

class CFieldTestCase(unittest.TestCase):

    def test_field(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) * 2)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X._pack_, 1)

    def test_pack_0(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
            _pack_ = 0
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(
