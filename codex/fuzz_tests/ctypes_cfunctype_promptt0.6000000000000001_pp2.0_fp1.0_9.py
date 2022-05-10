import ctypes
# Test ctypes.CFUNCTYPE
try:
    from _ctypes import CFuncPtr
except ImportError:
    CFuncPtr = None

import unittest
from test import support

class CFuncTestCase(unittest.TestCase):
    def test_basic(self):
        # test basic functionality
        from _ctypes import PyObj_FromPtr
        dll = ctypes.CDLL(support.TESTFN)
        #XXX: Win64
        func = CFuncPtr(None, ctypes.c_int, ctypes.c_int)
        func.__flags__ = ctypes.FUNCFLAG_CDECL
        func.__restype__ = ctypes.c_int
        func.__argtypes__ = (ctypes.c_int, ctypes.c_int)
        func.__name__ = 'my_func'

        ptr = ctypes.cast(dll._handle, ctypes.c_void_p).value + dll._func_flags_offset
        flags = ctypes.c_int.from_address(ptr).value
        self.assertEqual(flags
