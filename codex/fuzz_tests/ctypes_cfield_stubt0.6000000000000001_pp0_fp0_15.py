import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.CField * 5)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.CField * 5),
                ('c', ctypes.c_float)]

import unittest
from test import test_support

class ArrayTestCase(unittest.TestCase):
    def test_simple(self):
        c = C()
        self.assertEqual(c.a, 0)
        self.assertEqual(len(c.b), 5)
        self.assertEqual(c.b[2], 0)
        c.b[2] = 42
        self.assertEqual(c.b[2], 42)
        self.assertRaises(IndexError, c.b.__setitem__, 5, 42)

    def test_offsetof(self):
        self.assertEqual(ctypes.sizeof
