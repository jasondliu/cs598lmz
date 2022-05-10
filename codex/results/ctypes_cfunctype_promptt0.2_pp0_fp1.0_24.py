import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print(cmp_func(1, 2))

# Test ctypes.POINTER
POINTER_INT = ctypes.POINTER(ctypes.c_int)

# Test ctypes.byref
i = ctypes.c_int(0)
print(ctypes.byref(i))

# Test ctypes.string_at
s = b'hello world'
print(ctypes.string_at(s, 5))

# Test ctypes.memmove
a = (ctypes.c_byte * 10)()
b = (ctypes.c_byte * 10)(*range(10))
ctypes.memmove(a, b, 10)
print(a[:])

# Test ctypes.cast
a = (ctypes.c_byte * 10)(*range(10))
i
