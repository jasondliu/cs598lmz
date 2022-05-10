import ctypes
# Test ctypes.CFUNCTYPE interface

from ctypes import *
import unittest


class CFuncPtrTestCase(unittest.TestCase):

    def test_CFUNCTYPE(self):
        # Workaround for http://bugs.python.org/issue15796
        funcptr = CFUNCTYPE(c_int, c_int, c_int)
        error_msg = funcptr.errcheck(lambda result, func, arguments: None)
        self.assertIsNone(error_msg)

    def test_return_None(self):
        # Workaround for http://bugs.python.org/issue15796
        if cdll.msvcrt is None:
            libc = CDLL(ctypes.util.find_library("c"))
        else:
            libc = cdll.msvcrt
        qsort = libc.qsort
        qsort.argtypes = c_char_p, c_int, c_int, CFUNCTYPE(c_int, c_void_p, c_void_p)
        qsort.restype = c_
