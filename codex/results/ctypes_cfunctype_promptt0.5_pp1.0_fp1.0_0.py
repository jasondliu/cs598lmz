import ctypes
# Test ctypes.CFUNCTYPE()

# test_cfunctype.py

import unittest
from test import support
from ctypes import *

# XXX More tests needed!

class CFuncTestCase(unittest.TestCase):

    def test_1(self):
        # Test the CFUNCTYPE() factory function
        py_object_p = POINTER(py_object)
        c_int_p = POINTER(c_int)
        c_char_p = POINTER(c_char)

        # XXX check that the calling convention is correct
        # XXX check that the argtypes are correct

        func = CFUNCTYPE(c_int, c_int)(lambda x: x)
        self.assertEqual(func(42), 42)

        func = CFUNCTYPE(py_object, py_object)(lambda x: x)
        self.assertEqual(func(42), 42)

        func = CFUNCTYPE(py_object, c_int)(lambda x: x)
        self.assertEqual(func(42), 42)

        func
