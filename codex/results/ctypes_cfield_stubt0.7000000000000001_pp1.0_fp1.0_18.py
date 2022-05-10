import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass
C._fields_ = [('a', ctypes.c_int), ('b', ctypes.c_float)]

import unittest
class StructTestCase(unittest.TestCase):
    def test_field_index(self):
        self.assertEqual(S._fields_.index('x'), 0)
        self.assertRaises(ValueError, S._fields_.index, 'foo')

    def test_field_getattr(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_field_setattr(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_field_delattr(self):
        s = S()
        self.assertEqual(s.x, 0)
        s.x = 42

