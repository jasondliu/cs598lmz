import ctypes
# Test ctypes.CFUNCTYPE to work on all supported platforms
import sys

import unittest
from test import test_support as support

import _ctypes_test

lib = support.load_library('_ctypes_test', _ctypes_test.__file__)

class CFunctionTypeTest(unittest.TestCase):
    def test_error(self):
        from ctypes import CFUNCTYPE

        py_func = lambda x: x
        c_func = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(py_func)
        # TODO: RESET lib._testfunc_i_i in between the following tests
        lib._testfunc_i_i.restype = c_func
        lib._testfunc_i_i(1) # no error
        lib._testfunc_i_i.argtypes = (c_func,)
        lib._testfunc_i_i(1) # no error
        lib._testfunc_i_i.errcheck = c_func
        lib._testfunc_i_i(1) # no error
