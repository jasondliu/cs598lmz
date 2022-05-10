import ctypes
# Test ctypes.CFUNCTYPE()
print(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
# Test ctypes.POINTER()
print(ctypes.POINTER(ctypes.c_int))

# Test ctypes.cast()
print(ctypes.cast(0, ctypes.c_int))

# Test ctypes.string_at()
print(ctypes.string_at(0))

# Test ctypes.wstring_at()
print(ctypes.wstring_at(0))

# test ctypes.byref()
print(ctypes.byref(ctypes.c_int(0)))

# Test ctypes.addressof()
print(ctypes.addressof(ctypes.c_int(0)))

# Test ctypes.create_string_buffer()
print(ctypes.create_string_buffer(b'', 0))

# Test ctypes.create_unicode_buffer()
print(ctypes.create_unicode_buffer(u'', 0))

# Test ctypes.get_
