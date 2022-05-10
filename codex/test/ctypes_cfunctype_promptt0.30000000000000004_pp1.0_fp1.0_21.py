import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

def func_ptr(a, b):
    return func(a, b)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
ptr = CALLBACK(func_ptr)

print(ptr(1, 2))

