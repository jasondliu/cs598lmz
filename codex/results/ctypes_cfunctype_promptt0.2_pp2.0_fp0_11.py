import ctypes
# Test ctypes.CFUNCTYPE

# This test is not complete.  It only tests the basic functionality.
# It does not test the full range of argument types and return types.

import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        # Simple test of CFUNCTYPE
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        restype = ctypes.c_int
        argtypes = (ctypes.c_int,)
        f = prototype(( "my_sqr", dll), ((restype, "result"), (argtypes, "value")))
        self.assertEqual(f(5), 25)

    def test_errcheck(self):
        # Test CFUNCTYPE with an errcheck function
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
