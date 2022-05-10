import ctypes
# Test ctypes.CField.__set__()

import unittest
from test import test_support

import _ctypes_test

class SetTestCase(unittest.TestCase):

    def test_set_readonly_field(self):
        o = _ctypes_test.ReadOnlyUnion()
        self.assertRaises(AttributeError, setattr, o, "a", 42)

    def test_set_readonly_field_in_subclass(self):
        class X(_ctypes_test.ReadOnlyUnion):
            pass
        o = X()
        self.assertRaises(AttributeError, setattr, o, "a", 42)

    def test_set_readonly_field_in_subclass_override(self):
        class X(_ctypes_test.ReadOnlyUnion):
            _fields_ = [("a", ctypes.c_int)]
        o = X()
        o.a = 42
        self.assertEqual(o.a, 42)

    def test_set_readonly_field_in_subclass_override_readonly(self
