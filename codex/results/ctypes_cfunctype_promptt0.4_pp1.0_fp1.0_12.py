import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support
from ctypes import *
from ctypes.test import is_resource_enabled

class CFuncPtrTestCase(unittest.TestCase):

    def test_simple(self):
        # Simple test for CFUNCTYPE
        CallBackType = CFUNCTYPE(c_int, c_int, c_int)
        self.failUnlessEqual(sizeof(CallBackType), sizeof(c_void_p))

        def func(a, b):
            return a * b

        cb = CallBackType(func)
        self.failUnlessEqual(cb(2, 8), 16)

    def test_simple_args(self):
        # Simple test for CFUNCTYPE with arguments
        CallBackType = CFUNCTYPE(c_int, c_int, c_int)
        self.failUnlessEqual(sizeof(CallBackType), sizeof(c_void_p))

        def func(a, b):
            return a * b

        cb = CallBackType(func, (
