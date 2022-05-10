import ctypes
# Test ctypes.CField

import unittest
from test import support
from ctypes import *

class CFoo(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class TestCField(unittest.TestCase):
    def test_field(self):
        self.assertEqual(CFoo.a.offset, 0)
        self.assertEqual(CFoo.b.offset, ctypes.sizeof(c_int))
        self.assertEqual(CFoo.c.offset, ctypes.sizeof(c_int)*2)

    def test_field_subclass(self):
        class CSubFoo(CFoo):
            _fields_ = [("d", c_int)]
        self.assertEqual(CSubFoo.a.offset, 0)
        self.assertEqual(CSubFoo.b.offset, ctypes.sizeof(c_int))
        self.assertEqual(CSubFoo.c.offset, ctypes.sizeof(
