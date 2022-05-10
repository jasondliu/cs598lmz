import ctypes
# Test ctypes.CFUNCTYPE and ctypes.PYFUNCTYPE (ctypes.CFUNCTYPE is
# used by the ctypes.util.find_library() function).

import unittest
from test import support

# Dummy function to use as parameter for CFUNCTYPE
def func():
    pass

class CFuncPtrTestCase(unittest.TestCase):

    def test_CFuncPtr(self):
        from ctypes import CFUNCTYPE, WINFUNCTYPE, PYFUNCTYPE
        from ctypes import c_int, c_void_p, c_char_p, py_object

        # CFUNCTYPE
        CFUNCTYPE(c_int)
        CFUNCTYPE(c_int, c_void_p)
        CFUNCTYPE(c_int, c_void_p, c_char_p)

        # WINFUNCTYPE
        WINFUNCTYPE(c_int)
        WINFUNCTYPE(c_int, c_void_p)
        WINFUNCTYPE(c
