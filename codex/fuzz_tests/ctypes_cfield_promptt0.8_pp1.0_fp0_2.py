import ctypes
# Test ctypes.CField and ctypes.C_STRUCT_FIELDS

import sys
import unittest
from ctypes import *
from ctypes.test import need_symbol

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("x", POINTER(X))]

class Z(Union):
    _fields_ = [("i", c_int),
                ("x", POINTER(X))]

class Test(unittest.TestCase):
    def test(self):
        from _ctypes import CField

        self.assertEqual(X._fields_, [CField("a", c_int, 0), CField("b", c_int, 4)])
        self.assertEqual(Y._fields_, [CField("a", c_int, 0), CField("x", POINTER(X), 4)])
        self.assertEqual(Z._fields_, [CField("i", c
