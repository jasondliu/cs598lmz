import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE(c_int, c_int)(5)

# Test ctypes.WINFUNCTYPE()
WINFUNCTYPE(c_int, c_int)(5)

# Test ctypes.PYFUNCTYPE()
PYFUNCTYPE(c_int, c_int)(5)

# Test ctypes.create_string_buffer()
create_string_buffer(b'a')

# Test ctypes.create_unicode_buffer()
create_unicode_buffer('a')

# Test ctypes.addressof()
addressof(create_string_buffer(b'a'))

# Test ctypes.sizeof()
sizeof(c_int)

# Test ctypes.byref()
byref(c_int(5))

# Test ctypes.cast()
cast(addressof(create_string_buffer(b'a')), POINTER(c_char))

# Test ctypes.pointer()
pointer(c_int(5))

# Test ctypes.Alignment()
