import ctypes
# Test ctypes.CField

# This test verifies that the CField constructor works as expected.
# The CField class is used to model non-static data members.

import unittest
from test import support

class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class CFieldTest(unittest.TestCase):

    def test_constructor(self):
        # The constructor should raise an error if the argument is not
        # a ctypes type
        self.assertRaises(TypeError, ctypes.CField, 0)

        # The constructor should raise an error if the second argument
        # is not a string
        self.assertRaises(TypeError, ctypes.CField, ctypes.c_int, 0)

        # The constructor should raise an error if the second argument
        # is an empty string
        self.assertRaises(ValueError, ctypes.CField, ctypes.c_int, "")

        # The constructor should raise an error if the second argument
        # is
