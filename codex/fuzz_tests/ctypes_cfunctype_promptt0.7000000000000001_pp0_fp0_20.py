import ctypes
# Test ctypes.CFUNCTYPE by creating a callback that gets an integer argument
# and returns a c_char_p.  This is used in the callback tests.
def _test_cfunc(n):
    return ctypes.c_char_p(b"hello %d" % n)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)

# Callback types
CFUNCTYPE = ctypes.CFUNCTYPE
WINFUNCTYPE = ctypes.WINFUNCTYPE

import unittest
from test import test_support

class CFuncPtrTestCase(unittest.TestCase):
    def test_paramflags(self):
        # test parameter flags
        c_test_paramflags = CFUNCTYPE(
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        # Make sure the flags are correct for the cdecl calling convention
        self.assertEqual(c_test_paramflags.argtypes[0]._is_
