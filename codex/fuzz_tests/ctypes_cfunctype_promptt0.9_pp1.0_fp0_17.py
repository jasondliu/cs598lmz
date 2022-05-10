import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
import ctypes.test
# Test ctypes.c_float with NaN
import math, ctypes, ctypes.test
# Test structure creation with pointers to pointers
import copy, ctypes, ctypes.test

class X(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(ctypes.c_int))]

class TestFromAddress(ctypes.test.TestCase):
    def test_pointers(self):
        for tp, value in (
                (ctypes.c_int, 123),
                (ctypes.c_double, 3.14),
                (ctypes.c_char*, 'x'),
                (ctypes.c_wchar*, u'x'),
                (ctypes.c_longlong, 123),
                (ctypes.c_ulonglong, 123),
                (ctypes.c_void_p, ctypes.cast(255, ctypes.c_void_p))):
            addr = c
