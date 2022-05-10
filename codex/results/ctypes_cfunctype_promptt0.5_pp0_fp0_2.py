import ctypes
# Test ctypes.CFUNCTYPE
#
# The CFUNCTYPE constructor is used to create C function pointer types.
# The first argument is the return type of the function, followed
# by the argument types.

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    @support.cpython_only
    def test_basic(self):
        self.assertEqual(ctypes.CFUNCTYPE(ctypes.c_int)().restype,
                         ctypes.c_int)
        self.assertEqual(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)().argtypes,
                         (ctypes.c_int,))
        self.assertEqual(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)().argtypes,
                         (ctypes.c_int, ctypes.c_int))

    @support.cpython_only
    def test_default_args(self):
        # Default args are not
