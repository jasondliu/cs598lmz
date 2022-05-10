import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
#
# prototype:
#   int callit(int(*func)(int), int arg)

CALLIT = lib.callit
CALLIT.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
CALLIT.restype = ctypes.c_int

def func(arg):
    return arg + 42

result = CALLIT(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func), 5)
if result != 47:
    raise RuntimeError("wrong result")

# call a function with a function pointer argument
#
# prototype:
#   int callit_i(int(*func)(int), int arg)

CALLIT_I = lib.callit_i
CALLIT_I.argtypes = ctypes.CFUNCTYPE(ctypes.c
