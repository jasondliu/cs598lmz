import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test of the ctypes.CFUNCTYPE function. This function is used
# to create a ctypes function prototype object, which is used to define
# how to call a C function.
#
# This test exercises the ctypes.CFUNCTYPE function.
#
# This test was written by Thomas Heller.

import unittest

from ctypes import *

class CFUNCTYPETest(unittest.TestCase):
    def test_1(self):
        from ctypes import c_int, c_char_p, CFUNCTYPE
        prototype = CFUNCTYPE(c_int, c_char_p)
        self.assertEqual(prototype.argtypes, (c_char_p,))
        self.assertEqual(prototype.restype, c_int)

        prototype = CFUNCTYPE(c_int, c_char_p, c_int)
        self.assertEqual(prototype.argtypes, (c_char_p, c_int))
