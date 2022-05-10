import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_basic(self):
        # Check CFUNCTYPE() with basic argument and return types
        c_int_p = ctypes.POINTER(ctypes.c_int)
        prototype = ctypes.CFUNCTYPE(c_int_p, c_int_p)
        self.assertEqual(prototype.argtypes, (c_int_p,))
        self.assertEqual(prototype.restype, c_int_p)

    def test_callback(self):
        # Check CFUNCTYPE() with a callback function
        callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, callback)
        self.assertEqual(prototype.argtypes, (callback,))
        self.assertEqual(prototype.restype, ctypes.c_int)

@unittest.skip
