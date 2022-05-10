import ctypes
# Test ctypes.CFUNCTYPE()
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Test ctypes.POINTER()
ctypes.POINTER(ctypes.c_int)

# Test ctypes.c_int()
ctypes.c_int(42)

# Test ctypes.c_int.from_param()
ctypes.c_int.from_param(42)

# Test ctypes.c_void_p
ctypes.c_void_p(42)

# Test ctypes.c_char_p
ctypes.c_char_p(b"hello")

# Test ctypes.create_string_buffer()
ctypes.create_string_buffer(b"hello")

# Test ctypes.c_char_p.from_param()
ctypes.c_char_p.from_param(b"hello")

# Test ctypes.c_char_p.from_buffer()
ctypes.c_char_p.from_buffer(b"hello")

# Test ctypes.c_
