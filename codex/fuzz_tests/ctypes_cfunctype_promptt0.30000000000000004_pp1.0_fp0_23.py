import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer parameter

# The prototype is:
# int callit(int(*func)(int), int arg)

CALLIT = lib.callit
CALLIT.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
                   ctypes.c_int)
CALLIT.restype = ctypes.c_int

def func(arg):
    print("func", arg)
    return arg + 3

print(CALLIT(func, 5))

# call a function with a function pointer parameter
# The prototype is:
# int callit_p(int(*func)(char *), char *arg)

CALLIT_P = lib.callit_p
CALLIT_P.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p),
                     ctypes.c_char_p)
