import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# int callit(int(*func)(int), int arg)

CALLIT = lib.callit
CALLIT.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
CALLIT.restype = ctypes.c_int

def func(arg):
    print("func", arg)
    return arg + 3

print(CALLIT(func, 5))

# call a function with a function pointer argument
# this function is declared as:
# int callit_errcheck(int(*func)(int), int arg)

CALLIT_ERRCHECK = lib.callit_errcheck
CALLIT_ERRCHECK.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
CALLIT_
