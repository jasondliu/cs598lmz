import ctypes
# Test ctypes.CFUNCTYPE.
def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(func)
cfunc(1, 2)


# Test ctypes.CFUNCTYPE.
def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cfunc = CFunc(func)
cfunc(1, 2)


# Test ctypes.WinDLL.
