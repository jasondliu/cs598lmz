import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import need_symbol

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int),
                ("d", c_int)]

class Test(unittest.TestCase):
    def test_simple(self):
        callback = CFUNCTYPE(c_int, c_int, c_int)
        self.assertEqual(callback.argtypes, (c_int, c_int))
        self.assertEqual(callback.restype, c_int)

        # This is a function in _ctypes_
