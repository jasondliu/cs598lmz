import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE() factory function.
# It is also a test of the ctypes.c_int and ctypes.c_void_p types.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):
    def test_callbacks(self):
        # This test is for SF bug #1306942
        # Calling a callback with a wrong number of arguments segfaults
        import sys

        if sys.platform == "win32":
            windll.kernel32.GetVersion.restype = c_int
            windll.kernel32.GetVersion.argtypes = []

        def func():
            pass

        cb = CFUNCTYPE(c_int)(func)
        self.assertRaises(ArgumentError, cb, 1)

    def test_callback_returns_char_p(self):
        # Issue #12: Calling a callback that returns char * must return a
        # string, not a c_char_p instance.
        import sys


