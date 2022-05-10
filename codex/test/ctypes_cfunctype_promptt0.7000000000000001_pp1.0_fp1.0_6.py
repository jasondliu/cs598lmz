import ctypes
# Test ctypes.CFUNCTYPE()
#
# Sometimes the prototype is not available, so we must use stdcall.
#
# On windows, the stdcall calling convention is almost always used for
# windows API calls, and so we must use it for callbacks.  On unix,
# stdcall is not widely used, and so using it for callbacks is
# non-standard.  Therefore, on windows we use stdcall for callbacks,
# and the default for other platforms.
#
# If you want to use stdcall on non-windows platforms, define
# FORCE_STDCALL in your environment.
#
# This test also tests that the calling convention is correct if
# you pass None as the prototype.  The prototype must be correct
# for both windows and unix.

import sys, unittest
from ctypes import *

try:
    WinDLL
except NameError:
    WinDLL = None

if sys.platform == "win32":
    dll = WinDLL("kernel32")
    stdcall_flag = WINFUNCTYPE
else:
    dll = CDLL(None)

