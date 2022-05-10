import ctypes
# Test ctypes.CFUNCTYPE()

# This is a test of ctypes.CFUNCTYPE()

import ctypes
from ctypes import *
import unittest

class CFuncPtrTest(unittest.TestCase):
    def test_simple(self):
        # Simple function pointer
        CallbackType = CFUNCTYPE(c_int, c_int)
        self.failUnlessEqual(sizeof(CallbackType), sizeof(c_void_p))

        def func(arg):
            return arg + 1

        cb = CallbackType(func)
        self.failUnlessEqual(cb(5), 6)

    def test_simple_restype(self):
        # Simple function pointer with restype
        CallbackType = CFUNCTYPE(c_int, c_int)
        CallbackType.restype = c_int

        def func(arg):
            return arg + 1

        cb = CallbackType(func)
        self.failUnlessEqual(cb(5), 6)

