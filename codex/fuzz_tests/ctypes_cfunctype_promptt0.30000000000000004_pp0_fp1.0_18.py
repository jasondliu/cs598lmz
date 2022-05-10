import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(cfunc(1, 2))

# Test ctypes.POINTER
c_int_p = ctypes.POINTER(ctypes.c_int)
i = ctypes.c_int(42)
pi = ctypes.pointer(i)
print(pi.contents.value)

# Test ctypes.byref
print(ctypes.byref(i))

# Test ctypes.addressof
print(ctypes.addressof(i))

# Test ctypes.string_at
print(ctypes.string_at(ctypes.addressof(i), ctypes.sizeof(i)))

# Test ctypes.cast
print(ctypes.cast(ctypes.addressof(i), ctypes.POINTER(ctypes.c_char)))

# Test ctypes.memmove
s = b'Hello World
