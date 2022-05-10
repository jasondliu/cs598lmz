import ctypes
# Test ctypes.CField.from_address()

import unittest, sys
from test import test_support

class CF(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Test(unittest.TestCase):
    def test_from_address(self):
        import _ctypes_test
        p = _ctypes_test.POINTER(CF)()
        self.assertRaises(ValueError, p.contents.__setattr__, "a", 1)
        p.contents = ctypes.pointer(CF())
        p.contents.contents.a = 1
        self.assertEqual(p.contents.contents.a, 1)
        #
        self.assertRaises(ValueError, ctypes.CField.from_address, None, None)
        self.assertRaises(TypeError, ctypes.CField.from_address, None, ctypes.c_int)
        self.assertRaises(TypeError, ctypes.CField.from_address, ctypes.c_char_p,
