import ctypes
# Test ctypes.CFUNCTYPE() and argument coercion.

# From cpython/Lib/test/test_ctypes/test_cfunctype.py
import unittest

from ctypes import *
from ctypes.test import need_symbol

libc = cdll.msvcrt

def _test_function(fun):
    res = fun()
    if res != 42:
        raise AssertionError, hex(res)

class CFuncTypeTest(unittest.TestCase):
    def test_function(self):
        FUNCTYPE = CFUNCTYPE(c_int)
        self.assertEqual(FUNCTYPE.argtypes, None)
        self.assertEqual(FUNCTYPE.restype, c_int)

##    def test_function_callbacks(self):
##        # Check that the return value is converted according to the
##        # specified result type
##        FUNCTYPE = CFUNCTYPE(c_char, c_int)
##
##        @FUNCTYPE
##        def func(*args):
##
