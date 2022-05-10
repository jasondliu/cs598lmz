import ctypes
# Test ctypes.CField.

import unittest

class X(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int, 1), ("two", ctypes.c_int, 2)]

class Y(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int, 1), ("two", ctypes.c_int, 2)]

class TestCFields(unittest.TestCase):

    def test_bit_length(self):
        self.assertEqual(X.one.bit_length, 1)
        self.assertEqual(X.two.bit_length, 2)
        X.one.bit_length = 2
        self.assertEqual(X.one.bit_length, 2)
        self.assertEqual(X.two.bit_length, 2)
        def assign_negative_to_bit_length():
            X.one.bit_length = -1
        self.assertRaises(ValueError, assign_negative_to_bit_length)
        
    def test_offset(self
