import ctypes
# Test ctypes.CFUNCTYPE
#
# Test if:
#
# 1) A callback function receives the correct number of arguments
# 2) A callback function receives the correct types of arguments
#

# argtypes of the callback is None

def func(a):
    return a + 1

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

if cb(1) != 2:
    raise RuntimeError("callback function didn't receive the correct number of arguments")

# argtypes of the callback is not None

def func(a, b, c):
    return a + b + c

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

if cb(1, 2, 3) != 6:
    raise RuntimeError("callback function didn't receive the correct number of arguments")

# argtypes of the callback is not None:
# the argtype is not a ctypes type

