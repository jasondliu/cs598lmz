import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    return x + y

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.PYFUNCTYPE

def func(x, y):
    return x + y

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.WINFUNCTYPE

def func(x, y):
    return x + y

f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.FUNCFLAG_CDECL

def func(x, y):
    return x + y

f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.
