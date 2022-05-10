import ctypes
# Test ctypes.CFUNCTYPE with prototype that takes a "double *" as a parameter.
# The test fails when ctypes is compiled with MSVC.

def fn(*args):
    print(args)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_double))
CMPFUNC(fn)
