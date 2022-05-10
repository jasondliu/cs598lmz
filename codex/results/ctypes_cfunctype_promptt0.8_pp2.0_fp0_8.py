import ctypes
# Test ctypes.CFUNCTYPE().
#
import _ctypes_test

# This test only works with 32-bit ints
try:
    _ctypes_test.get_int_type(4)
except ValueError:
    import unittest
    raise unittest.SkipTest("requires 32-bit ints")

# Test creating a simple function type.
#
import _ctypes_test
lib = _ctypes_test.dll

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@func_type
def func(*args):
    return args[0] * 100 + args[1]

# Calling the function works:
res = func(5, 12)
if res != 512:
    raise RuntimeError("Calling func() returned %d instead of 512" % res)

# Set the ctypes.CFUNCTYPE instance as the function to call:
lib.set_callback.argtypes = ctypes.c_int, func_type
lib.set_callback.restype = ctypes.c_int

#
