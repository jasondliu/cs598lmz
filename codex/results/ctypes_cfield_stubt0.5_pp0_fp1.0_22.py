import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class E(C, D):
    _fields_ = [('z', ctypes.c_int)]

import unittest
from test import support

class Test(unittest.TestCase):
    def test_field_name(self):
        self.assertEqual(S.x.__name__, 'x')
        self.assertEqual(E.x.__name__, 'x')
        self.assertEqual(E.y.__name__, 'y')
        self.assertEqual(E.z.__name__, 'z')

    def test_field_type(self):
        self.assertEqual(type(S.x), ctypes.CField)
        self.assertEqual(type(E.x), ctypes.CField)
        self.assertEqual(type(E.
