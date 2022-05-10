import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTest(unittest.TestCase):

    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X._fields_[0][1]._type_, "i")
        self.assertEqual(X._fields_[0][1]._length_, 1)
        self.assertEqual(X._fields_[0][1]._offset_, 0)
        self.assertEqual(X._fields_[0][1]._index_, 0)
        self.assertEqual(X._fields_[0][1]._name_, "a")

    def test_array(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int * 3)]

        self.assertEqual(X._fields_[0][1]._type_, "i")
        self.assertEqual(X._fields_[
