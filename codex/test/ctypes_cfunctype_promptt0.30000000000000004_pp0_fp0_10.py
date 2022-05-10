import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

assert cfunc(1, 2) == 3

func_ptr = ctypes.cast(cfunc, ctypes.c_void_p).value

assert func_ptr != 0

cfunc = ctypes.cast(func_ptr, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))

assert cfunc(1, 2) == 3

# Test ctypes.WINFUNCTYPE

def func(a, b):
    return a + b

