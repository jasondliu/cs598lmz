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

wfunc_type = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
wfunc_c = wfunc_type(wfunc)
assert wfunc_c(0) == 0

# Test ctypes.PYFUNCTYPE

def pyfunc(n):
    return n

pyfunc_type = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
pyfunc_c = pyfunc_type(pyfunc)
assert pyfunc_c(0) == 0

# Test ctypes.CFUNCTYPE with an object as first argument

class X(object):
    def __
