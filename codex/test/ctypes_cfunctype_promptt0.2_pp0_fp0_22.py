import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    return x + y

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert f(1, 2) == 3

# Test ctypes.PYFUNCTYPE

def func(x, y):
    return x + y

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
assert f(1, 2) == 3

# Test ctypes.PYFUNCTYPE with keyword arguments

def func(x, y):
    return x + y

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
