import ctypes
# Test ctypes.CField with ctypes.wintypes.WORD, 
# ctypes.wintypes.DWORD, ctypes.wintypes.WCHAR, and 
# ctypes.wintypes.LPWSTR.
#
# This test should pass on all platforms, but it is 
# meaningful only on Windows.
#
# Create a test DLL that exposes the following functions:
#
# int __stdcall TestWORD(WORD *arg);
# int __stdcall TestDWORD(DWORD *arg);
# int __stdcall TestWCHAR(WCHAR *arg);
# int __stdcall TestLPWSTR(LPWSTR *arg);

import unittest
from ctypes import *
from ctypes.wintypes import *
import _ctypes_test

class CFieldsTestCase(unittest.TestCase):
    def test_WORD(self):
        class WORD_T(Structure):
            _fields_ = [("value", WORD)]
        w = WORD_T()
        w.value = 0x1234
        _ctypes_test
