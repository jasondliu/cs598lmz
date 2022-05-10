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

def get_ctypes_module():
    if sys.platform == 'win32':
        # On Windows, we need to use the ctypes module that is part of
        # the PyPy distribution.  This is because the ctypes module
        # that is part of CPython is a built-in extension module, and
        # it is not possible to import it from PyPy.

