import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    return a + b + c
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print cmp_func(2, 3)

# Test ctypes.WINFUNCTYPE
WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
win_func = WINFUNC(func)
print win_func(2, 3)

# Test ctypes.PYFUNCTYPE
PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
py_func = PYFUNC(func)
print py_func(2, 3)

# Test ctypes.c_void_p
def void_func(a):
    return a

VOIDFUNC = ctypes.CFUNCTY
