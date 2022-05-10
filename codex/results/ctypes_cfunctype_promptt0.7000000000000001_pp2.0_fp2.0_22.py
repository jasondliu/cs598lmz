import ctypes
# Test ctypes.CFUNCTYPE

import logging
logging.basicConfig(level=logging.DEBUG)

import unittest
from PyObjCTools.TestSupport import *

class TestCFuncType(unittest.TestCase):
    def testSimple(self):
        funcType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_float)
        self.assertEqual(funcType, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_float))

    def testCall(self):
        funcType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_float)

        @funcType
        def callme(a, b):
            return a * b

        self.assertEqual(callme(2, 3.14), 6.28)

    def testDefines(self):
        funcType = ctypes.CFUNCTYPE(
                None,
                ctypes.c_void_
