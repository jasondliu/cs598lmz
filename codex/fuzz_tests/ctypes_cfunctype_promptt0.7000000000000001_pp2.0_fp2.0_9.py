import ctypes
# Test ctypes.CFUNCTYPE.
#
# Usage: <this-test> <libtest_c.so>

import sys
import platform

from ctypes import *
from ctypes.test import need_symbol

import unittest

class CFunctionTypeTestCase(unittest.TestCase):

    def test_paramflags(self):
        # A function taking two ints and returning an int.
        FUNC = CFUNCTYPE(c_int, c_int, c_int)

        # Calling the function should give us back the sum.
        func = FUNC(lambda x, y: x + y)

        self.assertEqual(func(1, 2), 3)

        # The paramflags should be (1, 1, 0)
        self.assertEqual(func.argtypes, [c_int, c_int])
        self.assertEqual(func.restype, c_int)


    def test_simple(self):
        # A function taking two ints and returning an int.
        FUNC = CFUNCTYPE(c_int, c_int
