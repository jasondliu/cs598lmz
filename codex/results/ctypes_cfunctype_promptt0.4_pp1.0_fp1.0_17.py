import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    print 'func(%s, %s, %s)' % (a, b, c)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

cmp_func(1, 2, 3)

# Test ctypes.PYFUNCTYPE
PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

py_func = PYFUNC(func)

py_func(1, 2, 3)

# Test ctypes.WINFUNCTYPE
WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

win_func = WINFUNC(func)

win_func(1, 2, 3)
