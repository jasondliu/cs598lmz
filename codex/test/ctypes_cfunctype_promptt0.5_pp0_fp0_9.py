import ctypes
# Test ctypes.CFUNCTYPE
def func(x, f):
    return f(x)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def py_cmp(x, y):
    print("py_cmp", x, y)
    return x - y

