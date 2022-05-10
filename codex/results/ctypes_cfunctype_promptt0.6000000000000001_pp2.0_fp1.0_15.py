import ctypes
# Test ctypes.CFUNCTYPE
def c_func(a, b):
    return a + b

c_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

c_func_c = c_func_type(c_func)

print(c_func(1, 2))
print(c_func_c(1, 2))

# Test ctypes.CDLL
# ctypes.CDLL('libc.so.6')

# print(ctypes.cdll.LoadLibrary('libc.so.6'))

# Test ctypes.c_int
x = ctypes.c_int(42)
print(x)
print(x.value)

# Test ctypes.string_at
s = b"Hello World"
print(ctypes.string_at(id(s) + 5))

# Test ctypes.create_string_buffer
buf = ctypes.create_string_buffer(32)
print(buf.raw)

# Test ctypes.memmove

