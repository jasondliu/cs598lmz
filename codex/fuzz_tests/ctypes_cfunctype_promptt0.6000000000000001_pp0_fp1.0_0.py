import ctypes
# Test ctypes.CFUNCTYPE()
get_name = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
get_name(1)

# Test ctypes.POINTER()
get_name = ctypes.POINTER(get_name)
get_name(1)

# Test ctypes.addressof()
get_name = ctypes.addressof(get_name)
get_name(1)

# Test ctypes.cast()
get_name = ctypes.cast(get_name, ctypes.c_void_p)
get_name(1)

# Test ctypes.byref()
get_name = ctypes.byref(get_name)
get_name(1)

# Test ctypes.string_at()
get_name = ctypes.string_at(get_name)
get_name(1)

# Test ctypes.wstring_at()
get_name = ctypes.wstring_at(get_name)
get_name(1)

# Test ctypes.create_string
