import ctypes
# Test ctypes.CField() constructor.

from ctypes.test import need_symbol
import unittest, sys

class CFunctionsTestCase(unittest.TestCase):
    @staticmethod
    def callback(*args):
        return 42

    @staticmethod
    def errcheck(result, func, args):
        return result

    def test_simple_callbacks(self):
        # Callbacks with simple return type
        FUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
        CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int),
                                   ctypes.POINTER(ctypes.c_int))

        # Test function prototype
        f1 = FUNCTYPE(CFunctionsTestCase.callback)
        self.assertEqual(f1(), 42)
        f1(1, 2, 3)

        # Test set_conversion
        f2 = CMPFUNC(CFunctionsTestCase.errcheck)
        self.assertEqual(f2(None,
