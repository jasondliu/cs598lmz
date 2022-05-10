import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.PYFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.WINFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print f(1, 2)

# Test ctypes.CFUNCTYPE with a class

class X(object):
    def func(self, a, b):
        return a + b

f = ctypes.CFUNCTYPE(
