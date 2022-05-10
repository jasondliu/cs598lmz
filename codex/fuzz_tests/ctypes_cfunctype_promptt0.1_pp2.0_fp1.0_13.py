import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.  It is a bit more complicated than
# the other tests, because it has to create a function pointer type, and
# then create a function of that type.

import unittest
from test import support

import ctypes

class CFuncPtrTestCase(unittest.TestCase):

    def test_simple(self):
        # Simple test of ctypes.CFUNCTYPE.
        # Create a function pointer type, and then create a function of
        # that type.
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        paramflags = (1, "x")
        restype = ctypes.c_int
        check_result = _ctypes_test.get_check_result()
        def func(*args):
            return args[0] * 2
        func.__name__ = 'func'
        func.
