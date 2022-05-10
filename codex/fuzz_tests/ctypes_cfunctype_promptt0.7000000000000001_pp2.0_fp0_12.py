import ctypes
# Test ctypes.CFUNCTYPE
def myfunc(a, b):
    return a + b
myfunc = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(myfunc)
print ctypes.c_double(myfunc(1.0, 2.0))
# Test ctypes.cast
print ctypes.cast(ctypes.pointer(ctypes.c_double(3.0)), ctypes.POINTER(ctypes.c_int32))[0]
# Test ctypes.byref
print ctypes.byref(ctypes.c_double(4.0)).contents.value
# Test ctypes.addressof
print ctypes.addressof(ctypes.c_double(5.0))
# Test ctypes.create_string_buffer
print ctypes.create_string_buffer('foo')[:]
# Test ctypes.string_at
print ctypes.string_at(ctypes.create_string_buffer('foo'), 3)
# Test ctypes.wstring_at
print ctypes.wstring_at
