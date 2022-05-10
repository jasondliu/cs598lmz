import ctypes
# Test ctypes.CField

# This is a test of the CField structure.
#
# This structure is used to represent a single field in a
# ctypes Structure or Union.

import sys, unittest
from ctypes import *

class CFieldTest(unittest.TestCase):
    def test_1(self):
        class X(Structure):
            _fields_ = [("x", c_int)]

        class Y(Structure):
            _fields_ = [("y", c_int)]

        class Z(Structure):
            _fields_ = [("x", X), ("y", Y)]

        self.failUnlessEqual(Z.x.offset, 0)
        self.failUnlessEqual(Z.y.offset, sizeof(X))
        self.failUnlessEqual(sizeof(Z), sizeof(X) + sizeof(Y))

    def test_2(self):
        class X(Union):
            _fields_ = [("x", c_int)]

        class Y(Union):
            _fields_ = [("y", c_int)]

        class Z
