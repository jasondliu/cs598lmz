import ctypes
# Test ctypes.CField.

import ctypes
from ctypes import *
import unittest

class CFieldTestCase(unittest.TestCase):
    def test_basic(self):
        class X(Structure):
            _fields_ = [("a", c_int)]

        self.assertEqual(X._fields_[0][1], c_int)
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0]._type_, c_int)
        self.assertEqual(X._fields_[0]._name, "a")

    def test_field_arg(self):
        class X(Structure):
            _fields_ = [("a", c_int, 1)]

        self.assertEqual(X._fields_[0][1], c_int)
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][2], 1)
        self.assertEqual(X._fields_[
