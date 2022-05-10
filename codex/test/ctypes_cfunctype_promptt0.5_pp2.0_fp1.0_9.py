import ctypes
# Test ctypes.CFUNCTYPE.
# This is a bit tricky to test, since we need to make sure that the
# correct calling convention is used.  We do this by creating a
# function that calls back into Python, and then make sure that the
# callback actually gets called.

import sys

if sys.platform == 'win32':
    stdcall = ctypes.WINFUNCTYPE
    cdecl = ctypes.CFUNCTYPE
else:
    stdcall = ctypes.CFUNCTYPE
    cdecl = ctypes.CFUNCTYPE

