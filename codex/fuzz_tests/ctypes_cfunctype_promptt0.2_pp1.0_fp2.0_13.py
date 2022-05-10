import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print("py_cmp_func", a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

lib.call_cmp_func(cmp_func, 1, 2)

# call a function with a callback result

def py_inc_func(a):
    print("py_inc_func", a)
    return a + 1

INC_FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

inc_func = INC_FUNC(py_inc_func)

lib.call_inc_func(inc_func, 1)

# call a function with a callback argument and
