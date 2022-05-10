import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes test case in the Python 2.5.2
# distribution.

import unittest
from test import test_support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_basic(self):
        CFUNCTYPE = ctypes.CFUNCTYPE

        # CFUNCTYPE(restype, *argtypes)
        f = CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 42)
        self.assertEqual(f(1), 43)

        # CFUNCTYPE(restype, argtypes, use_errno=False, use_last_error=False)
        f = CFUNCTYPE(ctypes.c_int, [ctypes.c_int], use_errno=True)(lambda x: x + 42)
        self.assertEqual(f(1), 43)

        f = CFUNCTYPE(ctypes.c_int, [ctypes.c_int], use_last_
