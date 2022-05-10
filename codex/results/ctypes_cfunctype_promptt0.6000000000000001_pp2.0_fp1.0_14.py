import ctypes
# Test ctypes.CFUNCTYPE.

import unittest
from test.support import run_unittest

import _ctypes_test

class CFunctionTypeTestCase(unittest.TestCase):
    def test_simple_prototype(self):
        # Simple function prototype.
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(prototype.__name__, "CFUNCTYPE(c_int, c_int)")
        self.assertEqual(prototype(lambda x: x).__name__, "CFUNCTYPE(c_int, c_int)")
        self.assertEqual(prototype.__doc__, None)
        self.assertEqual(prototype(lambda x: x).__doc__, None)

        def callback(x):
            "callback function"
            return x

        prototype.__name__ = "my_callback"
        prototype.__doc__ = "my callback function"
        self.assertEqual(prototype.__name__, "my_callback")
        self.
