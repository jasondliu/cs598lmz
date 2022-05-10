import ctypes
# Test ctypes.CFUNCTYPE()

# This is a simple test of the CFUNCTYPE() function.  It is not
# intended to be complete.

import unittest
from test import test_support

class CFUNCTYPETest(unittest.TestCase):

    def test_basic(self):
        # Simple test of CFUNCTYPE()
        from ctypes import c_int, CFUNCTYPE
        Callable = CFUNCTYPE(c_int, c_int)
        self.assertEqual(Callable(42), 42)

    def test_errcheck(self):
        # Test the errcheck feature
        from ctypes import c_int, CFUNCTYPE
        def check_error(result, func, arguments):
            if result == -1:
                raise ValueError
            return result
        Callable = CFUNCTYPE(c_int, c_int, c_int,
                             errcheck=check_error)
        self.assertEqual(Callable(42, 0), 42)
        self.assertRaises(ValueError, Call
