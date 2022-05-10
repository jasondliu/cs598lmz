import ctypes
# Test ctypes.CFUNCTYPE

# NOTE: this test is not complete, it is just intended to test some
# corner cases.

import _ctypes
import unittest
from test import support

class CFUNCTYPETestCase(unittest.TestCase):

    def test_argtypes(self):
        # This tests that the argtypes tuple is correctly stored in the
        # _C_FUNC_TYPE_ARGTYPES attribute.
        def func(*args):
            pass
        self.assertEqual(ctypes.CFUNCTYPE(None)(func)._C_FUNC_TYPE_ARGTYPES, ())

        def func(a):
            pass
        self.assertEqual(ctypes.CFUNCTYPE(None)(func)._C_FUNC_TYPE_ARGTYPES, (ctypes.c_int,))

        def func(a, b):
            pass
        self.assertEqual(ctypes.CFUNCTYPE(None)(func)._C_FUNC_TYPE_ARGTYPES, (ctypes.c_int,
