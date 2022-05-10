import ctypes
# Test ctypes.CField
from ctypes import *

from ctypes.test import need_symbol

try:
    ctypes.CField
except AttributeError:
    raise unittest.SkipTest("This version of ctypes doesn't support CField")

class X(Structure):
    _fields_ = [("value", c_int)]

class Y(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

class Z(Structure):
    _fields_ = [("x", c_int)]

class Test(unittest.TestCase):

    def test_CField(self):
        self.assertEqual(X.value.offset, 0)
        self.assertEqual(X.value.size, sizeof(c_int))
        self.assertEqual(X.value.index, 0)

        self.assertEqual(Y.y.offset, sizeof(c_int))
        self.assertEqual(Y.y.size, sizeof(c_int))
        self.assertEqual(Y.y
