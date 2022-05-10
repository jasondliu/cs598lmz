import ctypes
# Test ctypes.CField.from_address
import _ctypes
import unittest

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class CFieldTestCase(unittest.TestCase):
    def test_from_address(self):
        x = X()
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(x)).value, 0)
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(x), 1).value, 0)
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(x), 2).value, 0)
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(x), 3).value, 0)
        self.assertRaises(ValueError, c
