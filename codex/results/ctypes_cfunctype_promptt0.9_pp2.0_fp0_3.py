import ctypes
# Test ctypes.CFUNCTYPE(...)(...) for multiple return values
from ctypes import *

import unittest
from test import test_support


@unittest.skipUnless(hasattr(ctypes, 'CFUNCTYPE'), 'requires CFUNCTYPE')
class CFuncTestCase(unittest.TestCase):
    # The callback functions:
    def func1(self, *args):
        return args[0] * 2
    def func2(self, *args):
        return args[0], args[2], args[1]
    def func3(self, arg):
        if isinstance(arg, int):
            return arg * 2, arg * 3
        else:
            return arg * arg, arg * arg * arg

    def test_count(self):
        # a function returning a single value, like, int.
        # check ctypes.c_int(self.func(c_int()))
        for type, param in zip(
                (c_int, c_long, c_short, c_double, c_float, c_longdouble, c_char_
