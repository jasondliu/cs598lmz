import ctypes
# Test ctypes.CFUNCTYPE().
# 
# This tests the feature that allows a function returing a pointer
# (or pointer-to-function) to be wrapped.
#
# It was added by Thomas Heller.

import _ctypes_test

libc = ctypes.CDLL(ctypes.util.find_library('c'))

getpid = libc.getpid
getpid.restype = ctypes.c_int

print(getpid())

getpid.restype = ctypes.c_void_p

print(getpid())
