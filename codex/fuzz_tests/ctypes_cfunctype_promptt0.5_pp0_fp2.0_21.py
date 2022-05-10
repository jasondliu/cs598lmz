import ctypes
# Test ctypes.CFUNCTYPE
#
# This test case is based on the ctypes tutorial:
# http://starship.python.net/crew/theller/ctypes/tutorial.html
#
# The original tutorial is in the public domain.

import unittest
from test import test_support

import ctypes

class CFuncPtrTestCase(unittest.TestCase):

    def test_CFUNCTYPE(self):
        # define a C function
        cmpfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int),
                                   ctypes.POINTER(ctypes.c_int))
        @cmpfunc
        def py_cmp(a, b):
            return a[0] - b[0]

        # Test the function
        a = (ctypes.c_int * 5)(5, 4, 3, 2, 1)
        qsort = ctypes.CDLL(None).qsort
        qsort.restype = None
        qsort.argtypes = (ctypes.c_void_p
