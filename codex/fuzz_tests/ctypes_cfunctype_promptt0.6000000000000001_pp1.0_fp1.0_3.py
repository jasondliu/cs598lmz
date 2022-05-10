import ctypes
# Test ctypes.CFUNCTYPE.

from ctypes import *
import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_function(self):
        prototype = CFUNCTYPE(c_int, c_int)
        paramflags = (1, "x"),
        self.assertEqual(prototype.argtypes, (c_int,))
        self.assertEqual(prototype.restype, c_int)
        self.assertEqual(prototype.errcheck, None)
        self.assertEqual(prototype.__name__, '<unknown>')
        self.assertEqual(prototype.__doc__, None)

    def test_function_with_name(self):
        prototype = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int, c_int,
                              c_int, c_int, c_int, c_int, c_int, c_int,
                              c_int, c_int, c_int, c_int, c_int,
