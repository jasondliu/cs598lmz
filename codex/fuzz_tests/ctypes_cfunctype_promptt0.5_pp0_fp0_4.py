import ctypes
# Test ctypes.CFUNCTYPE()

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# simple function

@CFUNCTYPE(c_int, c_int)
def func(*args):
    print("func", args)
    return args[0] * 2

lib.set_callback.argtypes = c_int, CFUNCTYPE(c_int, c_int)
lib.set_callback.restype = c_int

lib.call_callback.restype = c_int

lib.set_callback(1, func)
assert lib.call_callback() == 2

# function with strings

@CFUNCTYPE(c_int, c_char_p, c_int)
def func2(a, b):
    print("func2", repr(a), b)
    return b

lib.set_callback.argtypes = c_int, CFUNCTYPE(c_int, c_char_p, c_int)
lib.set_callback.restype = c_int

lib.
