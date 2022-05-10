import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print f(1)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
print f(1)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1, ())
print f(1)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1, ())
print f(1)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1, ())
print f(1)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1, ())
print f(1)

f
