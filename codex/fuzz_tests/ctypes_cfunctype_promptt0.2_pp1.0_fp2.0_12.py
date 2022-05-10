import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

# Test ctypes.POINTER
POINTER_int = ctypes.POINTER(ctypes.c_int)

# Test ctypes.byref
print ctypes.byref(ctypes.c_int(1))

# Test ctypes.cast
print ctypes.cast(ctypes.c_int(1), ctypes.c_int)

# Test ctypes.pointer
print ctypes.pointer(ctypes.c_int(1))

# Test ctypes.addressof
print ctypes.addressof(ctypes.c_int(1))

# Test ctypes.string_at
print ctypes.string_at(ctypes.c_int(1), 1)

# Test ctypes.wstring_at
print
