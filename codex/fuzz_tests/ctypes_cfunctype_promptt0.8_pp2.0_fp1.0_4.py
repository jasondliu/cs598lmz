import ctypes
# Test ctypes.CFUNCTYPE
i = 123
c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda i: i + 1)
print repr(c(i))

# Test the @ctypes.CFUNCTYPE decorator
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def f(i):
    return i + 1
print repr(f(i))

# Test ctypes.PYFUNCTYPE
i = 123
c = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda i: i + 1)
print repr(c(i))

# Test the @ctypes.PYFUNCTYPE decorator
@ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
def f(i):
    return i + 1
print repr(f(i))

# Test ctypes.WINFUNCTYPE
i = 123
c = ctypes.WINFUNCTYPE
