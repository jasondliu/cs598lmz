import ctypes
# Test ctypes.CFUNCTYPE.

import sys

if sys.platform != 'win32':
    import ctypes.wintypes

import unittest


class CFunctionTypeTest(unittest.TestCase):

    @unittest.skipIf(sys.platform != 'win32', 'Windows only test')
    def test_wintypes(self):
        WINFUNCTYPE = ctypes.WINFUNCTYPE
        MAX_PATH = 260

        GetModuleFileName = ctypes.windll.kernel32.GetModuleFileNameA
        GetModuleFileName.restype = ctypes.wintypes.DWORD
        GetModuleFileName.argtypes = (
            ctypes.wintypes.HMODULE, ctypes.wintypes.LPSTR, ctypes.
            wintypes.DWORD)

        @WINFUNCTYPE(ctypes.wintypes.HMODULE, ctypes.c_char_p)
        def GetModuleHandle(module_name):
            pass

        NULL = ctypes.wintypes.HMODULE(0)
        GetModuleHandle.
