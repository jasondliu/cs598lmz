import ctypes
# Test ctypes.CFUNCTYPE.  This must be done separately from test_ctypes, since
# on some platforms (OS X 10.6 or 10.7) ctypes will segfault when imported at
# module level.
import unittest
from test import test_support


class CFuncPtrTestCase(unittest.TestCase):
    def test_call(self):
        # Issue #7795: ctypes.CFUNCTYPE(restype, *argtypes)(func) must work
        from ctypes import c_int
        CFuncPtr = ctypes.CFUNCTYPE(c_int, c_int)
        func = CFuncPtr(lambda x: x + 42)
        self.assertEqual(func(5), 47)

    def test_paramflags(self):
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)
        # _ctypes_test.paramflags_test_1.argtypes = (ctypes.c_int, ctypes.c_int)
        func = dll._testfunc_p_
