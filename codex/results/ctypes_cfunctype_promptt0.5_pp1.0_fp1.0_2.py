import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print ("%d" % cmp_func(10, 20))

# Test ctypes.PYFUNCTYPE
def py_func(a, b):
    return a + b

CMPFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(py_func)

print ("%d" % cmp_func(10, 20))
