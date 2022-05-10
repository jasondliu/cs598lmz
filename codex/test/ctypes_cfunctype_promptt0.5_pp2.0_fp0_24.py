import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import unittest

from ctypes import *

class CFunctionTypeTestCase(unittest.TestCase):
    def test_prototype(self):
        prototype = CFUNCTYPE(c_int, c_int, c_int)
        self.assertEqual(prototype.__name__, "CFunctionType")

    def test_argtypes(self):
        prototype = CFUNCTYPE(c_int, c_int, c_int)
        self.assertEqual(prototype.argtypes, (c_int, c_int))

    def test_restype(self):
        prototype = CFUNCTYPE(c_int, c_int, c_int)
        self.assertEqual(prototype.restype, c_int)

    def test_errcheck(self):
        def errcheck(result, func, args):
            return args[0] + args[1]
        prototype = CFUNCTYPE(c_int, c_int, c_int, errcheck=errcheck)
        self.assertEqual
