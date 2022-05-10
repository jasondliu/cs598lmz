import ctypes
# Test ctypes.CField

import operator
import unittest
from test import test_support

# Simple structure.
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class FIELD(unittest.TestCase):
    def test_offsetof(self):
        field = POINT._fields_[0]
        self.assertRaises(NotImplementedError, operator.attrgetter(field[0]), POINT)
        self.assertEqual(ctypes.c_int.in_dll(POINT, field[0]).value, 0)

    def test_sizeof(self):
        self.assertEqual(ctypes.sizeof(POINT), 8)

    def test_flags(self):
        self.assertEqual(POINT._fields_[0][2], 0)

    def test_length(self):
        self.assertEqual(POINT._fields_[0][3], 1)

    def test_doc(self):
        self.assertE
