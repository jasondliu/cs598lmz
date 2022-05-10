import ctypes
# Test ctypes.CFUNCTYPE.

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_basic(self):
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(prototype(lambda x: x+1)(41), 42)

    def test_errcheck(self):
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                     errorcheck=lambda result, func, arguments: arguments[0] * 2)
        self.assertEqual(prototype(lambda x: x+1)(41), 82)

    def test_restype(self):
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                     restype=ctypes.c_int)
        self.assertEqual(prototype(lambda x: x+1)(41), 42)

    def test_argtypes(self):
        prototype = ctypes.CFUNCTY
