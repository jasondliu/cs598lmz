import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
import _ctypes_test

# Issue #6: ctypes.CFUNCTYPE(c_int) was not callable.
#
# This is fixed by patch #7

if _ctypes_test.test_cfunc_1(c_int(10), CFUNCTYPE(c_int)) != 10:
    raise RuntimeError("wrong result")

if _ctypes_test.test_cfunc_1(c_int(10), CFUNCTYPE(c_int, c_int)) != 10:
    raise RuntimeError("wrong result")

if _ctypes_test.test_cfunc_2(c_int(10), CFUNCTYPE(c_int)) != 10:
    raise RuntimeError("wrong result")

if _ctypes_test.test_cfunc_2(c_int(10), CFUNCTYPE(c_int, c_int)) != 10:
    raise RuntimeError("wrong result")

# Issue #7: ctypes.CFUNCTYPE(c_int)(lambda x
