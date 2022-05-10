import ctypes
# Test ctypes.CFUNCTYPE()

def func(a, b):
    return (a + b)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print(f(2, 3))

# Test ctypes.POINTER()

def func2(a, b):
    return (a + b)

f2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func2)

f2_ptr = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))(f2)

