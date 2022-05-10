import ctypes
# Test ctypes.CFUNCTYPE

import sys
import unittest
from test import support

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

class CFunctionTypeTestCase(unittest.TestCase):

    def test_argtypes(self):
        # ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
        # argtypes must be a tuple of ctypes types
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int)
        self.assertRaises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_int)
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                         use_errno=True)
