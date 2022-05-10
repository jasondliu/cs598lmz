import ctypes
# Test ctypes.CField, ctypes.CStruct, and ctypes.CUnion.
from _ctypes_test import func, func_si
from ctypes import *
import unittest
from test import test_support

class StructUnionTestCase(unittest.TestCase):
    def test_field_order(self):
        class X(Structure):
            _fields_ = [('a', c_int), ('b', c_int)]

        self.assertEqual(X._fields_[0][0], 'a')
        self.assertEqual(X._fields_[1][0], 'b')

        class Y(Structure):
            _fields_ = [('b', c_int), ('a', c_int)]

        self.assertEqual(Y._fields_[0][0], 'b')
        self.assertEqual(Y._fields_[1][0], 'a')

    def test_anonymous_struct(self):
        class X(Structure):
            _fields_ = [('a', c_int), ('b', c_int)]

        class Y(St
