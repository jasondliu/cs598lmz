import ctypes
# Test ctypes.CField
#

import unittest
from test import test_support

from ctypes import *

class FieldTestCase(unittest.TestCase):

    def test_basic(self):
        class X(Structure):
            _fields_ = [("a", c_int)]
        self.assertEqual((X._fields_[0][0], X._fields_[0][1]), ("a", c_int))

    def test_subclass_add_field(self):
        class Z(Structure):
            _fields_ = [("a", c_int)]
        class Y(Z):
            _fields_ = Z._fields_ + [("b", c_int)]
        class X(Y):
            _fields_ = Y._fields_ + [("c", c_int)]
        self.assertEqual(len(X._fields_), 3)
        self.assertEqual(X._fields_[0], ("a", c_int))
        self.assertEqual(X._fields_[1], ("b", c_int))
        self.assertEqual
