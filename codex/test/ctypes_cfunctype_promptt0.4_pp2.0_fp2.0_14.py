import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the fix of http://bugs.python.org/issue1202.
# The problem was that calling a callback function with the wrong
# number of arguments would segfault.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):
    def test_call_wrong_argc(self):
        # Calling a callback function with the wrong number of arguments
        # should raise a TypeError
        f = CFUNCTYPE(c_int, c_int)(lambda x: x)
        self.assertRaises(TypeError, f)
        self.assertRaises(TypeError, f, None)
        self.assertRaises(TypeError, f, None, None)
        self.assertRaises(TypeError, f, None, None, None)

