import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

from ctypes import *
from ctypes.test import need_symbol
from test.test_support import run_unittest
from test import test_support

################################################################

class CFuncPtrTestCase(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def check_type(self, ft, argtypes, restype):
        func = CFUNCTYPE(ft, *argtypes)(self.callback)
        self.assertEqual(func.argtypes, argtypes)
        self.assertEqual(func.restype, restype)
        return func

    def check_basic_types(self, argtypes, restype):
        func = self.check_type(restype, argtypes, restype)
        res = func(*[restype(i) for i in range(len(argtypes))])
        self.assertEqual(res, restype(len(argtypes) - 1))
        self.assertEqual(self.
