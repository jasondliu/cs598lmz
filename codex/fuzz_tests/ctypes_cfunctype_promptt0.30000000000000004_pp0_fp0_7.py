import ctypes
# Test ctypes.CFUNCTYPE

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(a):
    return a + 1

assert func(1) == 2

# Test ctypes.WINFUNCTYPE

@ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(a):
    return a + 1

assert func(1) == 2

# Test ctypes.PYFUNCTYPE

@ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(a):
    return a + 1

assert func(1) == 2
