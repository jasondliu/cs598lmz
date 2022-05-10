import ctypes
# Test ctypes.CFUNCTYPE, with several calling conventions
from ctypes import *
from ctypes.test import is_resource_enabled
import unittest

class CFuncPtrTestCase(unittest.TestCase):
    def test_prototype(self):
        self.assertRaises(TypeError, CFUNCTYPE, 42)
        self.assertRaises(TypeError, CFUNCTYPE, 42, 42)

        # check for keyword arguments
        self.assertRaises(TypeError, CFUNCTYPE, c_int, argtypes=[c_int])
        CFUNCTYPE(None, argtypes=[c_int], restype=c_int)

    def test_argtypes(self):
        prototype = CFUNCTYPE(c_int, c_int)
        self.assertRaises(TypeError, prototype, "spam")
        self.assertRaises(TypeError, prototype, 42)

        @prototype
        def func(*args):
            return len(args)

        self.assertEqual(func(1, 2, 3), 3)

    def test_errcheck
