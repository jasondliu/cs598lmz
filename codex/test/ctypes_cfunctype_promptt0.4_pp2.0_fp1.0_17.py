import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x*x

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print(cmp_func(3))

# Test ctypes.POINTER
POINTER_INT = ctypes.POINTER(ctypes.c_int)

i = ctypes.c_int(10)

p = ctypes.pointer(i)

print(p)
print(p.contents)
print(p.contents.value)

# Test ctypes.byref
i = ctypes.c_int(10)

p = ctypes.byref(i)

print(p)
