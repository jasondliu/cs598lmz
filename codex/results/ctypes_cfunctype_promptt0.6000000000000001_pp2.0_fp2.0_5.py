import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        # prototype of the function is:
        # int func(int)
        func = dll._testfunc_i_i
        func.argtypes = ctypes.c_int,
        func.restype = ctypes.c_int
        self.assertEqual(func(5), 6)

        func.argtypes = ctypes.c_char,
        func.restype = ctypes.c_char
        self.assertEqual(func(b'x'), b'y')

        # Now create the function type:
        CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        # And call it
        self.assertEqual(CMPFUNC(func)(5), 6)

        # prototype of the function is:
       
