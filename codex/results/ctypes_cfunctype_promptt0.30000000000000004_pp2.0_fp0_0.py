import ctypes
# Test ctypes.CFUNCTYPE

import sys

if sys.platform == 'win32':
    from ctypes import wintypes
    from ctypes.wintypes import BOOL, HWND, LPCSTR, LPVOID, UINT
    prototype = ctypes.WINFUNCTYPE
    paramflags = (1, "hwnd", 0), (1, "lpszString", "Hello"), (1, "uFlags", 0), (1, "lParam", None)
else:
    prototype = ctypes.CFUNCTYPE
    paramflags = (1, "hwnd"), (1, "lpszString", "Hello"), (1, "uFlags", 0), (1, "lParam", None)

MessageBox = prototype(BOOL, HWND, LPCSTR, LPCSTR, UINT)
MessageBox.errcheck = ctypes.check_bool
MessageBox.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBox.restype = BOOL

MessageBox.__doc__ = """MessageBox(hwnd, lpszString, lps
