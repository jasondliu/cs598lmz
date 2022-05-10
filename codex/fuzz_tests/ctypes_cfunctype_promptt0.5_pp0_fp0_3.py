import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x+1

cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

print cf(1)

# Test ctypes.PYFUNCTYPE

def func(x):
    return x+1

pf = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

print pf(1)

# Test ctypes.WINFUNCTYPE

def func(x):
    return x+1

wf = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

print wf(1)
