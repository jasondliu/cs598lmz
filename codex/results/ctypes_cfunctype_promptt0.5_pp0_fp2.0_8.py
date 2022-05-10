import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes
import unittest

from ctypes import *

# XXX This is a hack:
# For some reason on Windows 64bit, the 'restype' of the callback
# function is not set by the CFUNCTYPE() constructor.  I don't know
# why, but this hack works around the problem.
try:
    WINFUNCTYPE
except NameError:
    def WINFUNCTYPE(restype, *argtypes):
        return CFUNCTYPE(restype, *argtypes)

class X(Structure):
    _fields_ = [("a", c_int)]

class CFuncPtrTestCase(unittest.TestCase):
    def test_1(self):
        f = CFUNCTYPE(c_int)
        self.assertEqual(sizeof(f), sizeof(c_void_p))
        self.assertEqual(f.__name__, "CFUNCTYPE(c_int)")
        self.assertEqual(f.__doc__, "function (c_int)")
