import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not complete.  It tests the most common uses of
# ctypes.CFUNCTYPE.  The remaining tests are in test_cfunctype.py.

import unittest
from test import support

import _ctypes_test
dll = _ctypes_test.dll

class CFuncPtrTestCase(unittest.TestCase):

    def test_argtypes(self):
        # The argtypes attribute must be a tuple, even if only
        # one type is passed.
        CFUNCTYPE = ctypes.CFUNCTYPE

        f = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
        self.assertEqual(f.argtypes, (ctypes.c_int,))
        f = CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x)
        self.assertEqual(f.argtypes, (ctypes.c_int, ctypes.c_int))
