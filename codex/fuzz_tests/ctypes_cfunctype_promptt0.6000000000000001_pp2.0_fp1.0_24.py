import ctypes
# Test ctypes.CFUNCTYPE
def foo(a, b):
    return a + b
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(foo)
print f(1, 2)

# Test ctypes.POINTER
p = ctypes.POINTER(ctypes.c_int)
print p

# Test ctypes.create_string_buffer
b = ctypes.create_string_buffer("abc")
print b.raw
print b.value

# Test ctypes.string_at
b = ctypes.create_string_buffer("abc")
print ctypes.string_at(b)

# Test ctypes.cast
b = ctypes.create_string_buffer("abc")
p = ctypes.cast(b, ctypes.POINTER(ctypes.c_char))
print p.contents.value

# Test ctypes.memset
p = ctypes.create_string_buffer("abc")
ctypes.memset(p, 0, 1)
print p.raw

# Test c
