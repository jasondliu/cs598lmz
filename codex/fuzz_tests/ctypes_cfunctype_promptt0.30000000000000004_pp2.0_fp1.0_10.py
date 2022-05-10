import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print cmp_func(1, 2)

# Test ctypes.PYFUNCTYPE
def pyfunc(a, b):
    return a + b

PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

py_func = PYFUNC(pyfunc)
print py_func(1, 2)

# Test ctypes.WINFUNCTYPE
def winfunc(a, b):
    return a + b

WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

win_func = WINFUNC(winfunc)
print win_func(1, 2)

# Test
