import ctypes
# Test ctypes.CField()

# This is a test of the ctypes.CField() class.

# The CField class is a helper class.  It allows you to create
# a class which has a ctypes type as a member, and a pointer to
# that type.  For example, the following creates a class which
# has a member called 'foo' which is an integer and a member
# called 'pfoo' which is a pointer to an integer.

# Note: This is not meant to be a full test of the CField class.
# It is just a basic test to ensure that the class works as
# intended.

import unittest
from ctypes import *

class TestCField(unittest.TestCase):
    def test_basic(self):
        class X(Structure):
            _fields_ = [
                ("foo", c_int),
                ("pfoo", POINTER(c_int))
            ]
        x = X()
        x.foo = 42
        self.assertEqual(x.foo, 42)
        self.assertEqual(x.pfoo[0],
