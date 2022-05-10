import ctypes
# Test ctypes.CFUNCTYPE()
#
# This test is not really complete or useful, but it does at least
# test that the CFUNCTYPE() factory function is available.

import _ctypes_test

try:
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
except AttributeError:
    raise ImportError("This test requires ctypes")

@prototype
def func(n):
    "Python function"
    print('func', n)
    return n * 10

##print func(42)

lib = ctypes.CDLL(_ctypes_test.__file__)
lib.set_func.argtypes = ctypes.c_int,
lib.set_func.restype = ctypes.c_void_p
lib.set_func(func)

lib.call_func.argtypes = ctypes.c_int,
lib.call_func.restype = ctypes.c_int
result = lib.call_func(42)

##print result

if result != func(42):
    raise
