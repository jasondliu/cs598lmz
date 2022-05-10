import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(cfunc(1, 2))

# Test ctypes.byref
a = ctypes.c_int(1)
b = ctypes.c_int(2)
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(cfunc(a, b))
print(a.value)
print(b.value)

# Test ctypes.byref
a = ctypes.c_int(1)
b = ctypes.c_int(2)
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(cfunc(ctypes.byref(a), ctypes.byref(b)))
print(a.value)
print(
