import ctypes
# Test ctypes.CFUNCTYPE
def foo(a, b):
    return a+b

foo_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print(foo_ptr(1, 2))

foo_ptr = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(foo)
print(foo_ptr(1, 2))

foo_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print(foo_ptr(1, 2))

foo_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print(foo_ptr(1, 2))

foo_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print(foo_ptr(1, 2))

