import ctypes
# Test ctypes.CFUNCTYPE
from ctypes.test import need_symbol

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int)]

class Z(Structure):
    _fields_ = [("a", c_int)]

class Test(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        # Check the argtypes attribute

        CMPFUNC = CFUNCTYPE(c_int, POINTER(X), POINTER(X))
        qsort = lib.my_qsort
        qsort.argtypes = (c_void_p, c_size_t, c_size_t, CMPFUNC)
        qsort.restype = None

        l = list(range(10))
        a = (X * len(
