import ctypes
# Test ctypes.CFUNCTYPE(), and if it can be called in two ways:
#
#     CFUNCTYPE(restype, *argtypes)(callable)
#     CFUNCTYPE(restype, *argtypes)(address, [optional_flags])

import unittest
from test.support import is_resource_enabled, run_unittest

from ctypes import *
from ctypes.test import need_symbol

try:
    WinDLL
except NameError:
    WinDLL = CDLL

dll = CDLL(None)

# The following functions all return int and have no arguments
# so we can use them to test different features of ctypes

if is_resource_enabled("POSIX"):
    from ctypes import _posix_functions
    _posix_functions._getpid = dll._getpid

try:
    SetLastError = WINFUNCTYPE(c_int, c_int)(("SetLastError", dll))
    GetLastError = WINFUNCTYPE(c_int)(("GetLastError", dll))
except Att
