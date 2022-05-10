import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', S)]

ctypes.CStructure = type(S)
ctypes.CUnion = type(ctypes.c_int)

import unittest
from test import test_support

class ArrayTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        class Y(ctypes.Structure):
            _fields_ = [("b", ctypes.c_int),
                        ("c", ctypes.c_int * 2)]

        # A pointer to an array of two Y structures:
        class Z(ctypes.Structure):
            _fields_ = [("d", ctypes.POINTER(Y * 2))]

        # A pointer to an array of three X structures:
        class W(ctypes.Structure):
            _fields_ = [("e", ctypes.POINTER(X * 3))]

        x = X()

