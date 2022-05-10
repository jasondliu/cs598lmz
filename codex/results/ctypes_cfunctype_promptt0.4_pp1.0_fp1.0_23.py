import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_basic(self):
        c_int_p = ctypes.POINTER(ctypes.c_int)
        c_int_p_p = ctypes.POINTER(c_int_p)
        c_int_p_p_p = ctypes.POINTER(c_int_p_p)
        c_int_p_p_p_p = ctypes.POINTER(c_int_p_p_p)

        # This is the function type we will use in the callback
        # function
        FUNC = ctypes.CFUNCTYPE(c_int_p, c_int_p_p, c_int_p_p_p_p)

        # This is the callback function
        def func(a, b, c):
            self.assertEqual(a[0], 1)
            self.assertEqual(b[0][0], 2)
            self.assertEqual(c[0][0
