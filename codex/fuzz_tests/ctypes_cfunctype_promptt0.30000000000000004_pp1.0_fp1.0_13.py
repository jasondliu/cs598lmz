import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print(cmp_func(1, 2))

# Test ctypes.PYFUNCTYPE
PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

py_func = PYFUNC(func)
print(py_func(1, 2))

# Test ctypes.WINFUNCTYPE
WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

win_func = WINFUNC(func)
print(win_func(1, 2))

# Test ctypes.CFUNCTYPE(None)
def func():
    return None

CMPFUNC = ctypes.CFUNCT
