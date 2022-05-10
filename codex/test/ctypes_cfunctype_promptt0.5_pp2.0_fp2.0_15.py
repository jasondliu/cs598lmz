import ctypes
# Test ctypes.CFUNCTYPE.
def func(a):
    print(a)
    return a
CFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cf = CFuncType(func)
cf(1)

# Test ctypes.PYFUNCTYPE.
def func(a):
    print(a)
    return a
PyFuncType = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
pf = PyFuncType(func)
pf(1)

# Test ctypes.WINFUNCTYPE.
def func(a):
    print(a)
    return a
