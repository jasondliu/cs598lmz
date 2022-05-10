import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

assert f(1) == 2

# Test ctypes.PYFUNCTYPE

def func(x):
    return x + 1

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

assert f(1) == 2

# Test ctypes.WINFUNCTYPE

def func(x):
    return x + 1

f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

assert f(1) == 2

# Test ctypes.CFUNCTYPE(None)

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)

assert f(1) is None

# Test ctypes.PYFUNCTYPE(None
