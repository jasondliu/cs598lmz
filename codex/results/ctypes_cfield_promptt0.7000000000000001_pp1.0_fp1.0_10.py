import ctypes
# Test ctypes.CField.
################################################################################

import unittest
import sys

class CFieldTest(unittest.TestCase):

    def test_simple(self):
        class Bar(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]

        self.assertEqual(Bar.foo.offset, 0)
        self.assertEqual(Bar.foo.size, ctypes.sizeof(ctypes.c_int))

        # check assignment to the field
        b = Bar(1)
        self.assertEqual(b.foo, 1)
        b.foo = 42
        self.assertEqual(b.foo, 42)

        # check assignment to the field attribute
        Bar.foo = 3
        self.assertEqual(b.foo, 3)

        # check assignment to a plain attribute
        b.foo = 42
        self.assertEqual(b.foo, 42)
        b.bar = 42
        self.assertEqual(b.bar, 42)

    def test_subclass(self):
        class Bar(ct
