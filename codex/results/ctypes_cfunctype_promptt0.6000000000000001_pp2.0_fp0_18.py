import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = _ctypes_test.dll

if isinstance(ctypes.c_int, type(ctypes.c_int())):
    # ctypes.c_int is a class, not a factory function
    c_int = ctypes.c_int
else:
    # ctypes.c_int is a factory function
    c_int = ctypes.c_int()

def check_type(tp):
    print(tp)
    if tp is c_int:
        return 1
    return 0

CMPFUNC = ctypes.CFUNCTYPE(c_int, ctypes.c_int)

# call a function with a CFUNCTYPE argument
f = lib.TestFunc
f.argtypes = (CMPFUNC, ctypes.c_int)
f.restype = c_int

print(f(CMPFUNC(check_type), c_int(42)))

# assign a CFUNCTYPE to a function
f2 = lib.TestFunc2

