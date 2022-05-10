import ctypes
# Test ctypes.CFUNCTYPE()
def func(x, y):
    return x + y

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
f(1, 2)

# Test ctypes.CFUNCTYPE(restype=None, *argtypes)
def func2(x, y):
    return x + y

f2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func2)
f2(1, 2)

# Test ctypes.CFUNCTYPE(restype=None, *argtypes, use_errno=False, use_last_error=False)
def func3(x, y):
    return x + y

f3 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, use_errno=False, use_last_error=False)(func3)
f3(1, 2)

# Test ctypes.CFUNCTY
