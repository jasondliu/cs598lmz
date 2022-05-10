import ctypes
# Test ctypes.CField.from_param

import unittest
from test import test_support

class Struct1(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]


class Struct1Ptr(ctypes.POINTER(Struct1)):
    pass

class Struct2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.POINTER(Struct1))]


class Struct2Ptr(ctypes.POINTER(Struct2)):
    pass

class Struct3(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.POINTER(Struct2))]

class Struct3Ptr(ctypes.POINTER(Struct3)):
    pass


class FieldTest(unittest.TestCase):
    def test_field_to_param(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.
