import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
print f(42)

f = ctypes.CFUNCTYPE(ctypes.c_int
