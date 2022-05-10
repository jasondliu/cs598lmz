import ctypes
# Test ctypes.CFUNCTYPE -- this must be the first ctypes_test otherwise
# the callbacks are still registered to the lib and crashes python
# when it exists, at least on Linux.

import unittest
from ctypes_test.test.test_support import has_ruby, is_jython, is_freebsd, run_unittest

callbacks = []

# XtInputCallbackProc
CALLBACK = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p)

# XXX: The following for some strange reason only works on Windows, or if
# XXX: Python is also compiled with MSVC :-(
if sizeof(c_int) == sizeof(c_void_p):
    RESTYPE = c_void_p
else:
    RESTYPE = c_int

lib = CDLL(ctypes.util.find_library("c"))

# XtAppGetExitFlag
lib.XtAppGetExitFlag.restype = c_int

# XtAppInitialize
lib.XtAppInitialize.restype =
