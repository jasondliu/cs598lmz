import _struct
# Test _struct.Struct
print(_struct.Struct('i').size)

# Test py_object
p = ctypes.py_object()
p.value = "hello"
print(p.value)

# Test POINTER(c_char_p)
pp = ctypes.POINTER(ctypes.c_char_p)()
pp.contents = b"hello"
print(pp.contents)

# Test pointer()
print(ctypes.pointer(ctypes.c_int(42)))

# Test byref()
p = ctypes.c_int()
ctypes.pointer(p)[0] = 42
print(p.value)

# Test addressof()
a = (ctypes.c_int * 3)()
print(ctypes.addressof(a))
print(ctypes.addressof(a, 1))

# Test cast()
print(ctypes.cast(ctypes.c_int(42), ctypes.POINTER(ctypes.c_int)))

# Test c_buffer
p = ctypes.c_buffer(b"hello
