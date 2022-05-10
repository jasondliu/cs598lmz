import ctypes
# Test ctypes.CFUNCTYPE

# Basic test
def func_test(x):
    return x

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func_test)
if callback(42) != 42:
    raise RuntimeError('callback() returned wrong value')

# Test with arguments and return type
def func_test(x, y):
    return x * y

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func_test)
if callback(6, 7) != 42:
    raise RuntimeError('callback() returned wrong value')

# Test with too many arguments
def func_test(x, y):
    return x * y

try:
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(func_test)
except TypeError:
    pass
else:
    raise RuntimeError("Too many arguments didn't raise TypeError")

#
