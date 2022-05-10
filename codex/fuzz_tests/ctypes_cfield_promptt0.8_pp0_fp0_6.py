import ctypes
# Test ctypes.CField

import unittest
from test import support


class TestCField(unittest.TestCase):
    def test_access_variation(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_ubyte * 3 * 2 * 3 * 4 * 5 * 6 * 7 * 8)]

        x = X()
        self.assertEqual(len(x.a), 3 * 2 * 3 * 4 * 5 * 6 * 7 * 8)
        self.assertRaises(TypeError, setattr, x, "a", None)
        x.a[0] = 42
        self.assertEqual(x.a[0], 42)
        a_bytes = bytes(x.a)
        x.a = a_bytes
        self.assertEqual(type(x.a), type(a_bytes))


class TestPointer(unittest.TestCase):
    def test_init_retval(self):
        # Check that the default value returned by POINTER() is None
        self.assertIs(ct
