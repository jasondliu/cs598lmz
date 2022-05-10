import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a little more complicated than the other tests, because we
# want to test the functionality of ctypes.CFUNCTYPE itself, not just
# the functionality of the CFUNCTYPE instances.
#
# Therefore, we test that the CFUNCTYPE factory function returns the
# appropriate types for different kinds of functions, and then we test
# that the created types have the appropriate signatures.
#
# We don't test the actual calling of the functions, just the
# signatures.
import sys
import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def _check_type(self, restype, argtypes, check_paramflags):
        # Check that ctypes.CFUNCTYPE(restype, argtypes) returns the
        # appropriate type object.
        func = ctypes.CFUNCTYPE(restype, argtypes)
        self.assertEqual(func._restype_, restype)
        self.assertEqual(func._argtypes_, argtypes)
        # The _flags_ are
