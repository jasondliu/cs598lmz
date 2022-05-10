import ctypes
# Test ctypes.CFUNCTYPE()

# This test is a bit more complex than the others, because it has to
# work on both CPython and PyPy.  In CPython, the ctypes module is a
# built-in extension module, and we need to make sure that it works
# with the version of ctypes that comes with PyPy.  In PyPy, the
# ctypes module is written in RPython and translated into C, and we
# need to make sure that it works with the version of ctypes that
# comes with CPython.

import sys
if sys.platform == 'win32':
    from ctypes import windll, wintypes
    from ctypes.wintypes import BOOL, HWND, LPCSTR, LPVOID

