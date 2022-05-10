import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(f(1, 2))

# Test ctypes.POINTER
def func2(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(func2)
a = ctypes.c_int(1)
b = ctypes.c_int(2)
print(f(ctypes.byref(a), ctypes.byref(b)))

# Test ctypes.byref
def func3(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(func3)
a =
