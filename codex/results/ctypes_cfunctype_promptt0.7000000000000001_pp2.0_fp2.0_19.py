import ctypes
# Test ctypes.CFUNCTYPE.
import ctypes
import ctypes.util

import unittest

class CFunctionTypeTestCase(unittest.TestCase):
    def test_simple_arg(self):
        import sys
        if sys.platform == "win32":
            libm = ctypes.cdll.msvcrt
        else:
            libm = ctypes.cdll.LoadLibrary(ctypes.util.find_library("m"))

        sin = libm.sin
        sin.restype = ctypes.c_double
        sin.argtypes = ctypes.c_double,

        self.failUnlessEqual(sin(0), 0)

    def test_multiple_args(self):
        import sys
        if sys.platform == "win32":
            libm = ctypes.cdll.msvcrt
        else:
            libm = ctypes.cdll.LoadLibrary(ctypes.util.find_library("m"))

        memset = libm.memset
        memset.restype = ctypes.c_void_p
        memset.arg
