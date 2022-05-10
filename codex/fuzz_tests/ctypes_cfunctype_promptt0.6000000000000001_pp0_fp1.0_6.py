import ctypes
# Test ctypes.CFUNCTYPE

i = ctypes.c_int(1)
f = ctypes.c_float(1.2)

def func(i, f):
    return i + f

CFunc = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_int, ctypes.c_float)

cf = CFunc(func)

cf(i, f)

# Test ctypes.PYFUNCTYPE

def pyfunc(i, f):
    return i + f

PFunc = ctypes.PYFUNCTYPE(ctypes.c_float, ctypes.c_int, ctypes.c_float)

pf = PFunc(pyfunc)

pf(i, f)

# Test ctypes.WINFUNCTYPE

def winfunc(i, f):
    return i + f

WFunc = ctypes.WINFUNCTYPE(ctypes.c_float, ctypes.c_int, ctypes.c_float)

wf = WFunc(winfunc)
