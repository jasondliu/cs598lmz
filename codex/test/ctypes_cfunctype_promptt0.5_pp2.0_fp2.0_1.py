import ctypes
# Test ctypes.CFUNCTYPE
def cfunc(n):
    return n

cfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cfunc_c = cfunc_type(cfunc)
assert cfunc_c(0) == 0

# Test ctypes.WINFUNCTYPE

def wfunc(n):
    return n

