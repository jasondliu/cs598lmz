import ctypes
# Test ctypes.CField.from_address
from ctypes import * # old style


try:
    import _ctypes_test
except ImportError:
    try:
        import ctypes._ctypes_test
    except ImportError:
        import sys; sys.exit()

from ctypes import Structure, Union, c_int, c_char
import unittest
from test import test_support


class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int)]

class XX(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

class Y(Union):
    _fields_ = [("a", c_int),
                ("b", c_char)]


class TestField(unittest.TestCase):
    def test_field_in_structure(self):
        def func_in(x):
            return x.a

        def func_out(x):
            return x.a

        self.assertEqual(func_
