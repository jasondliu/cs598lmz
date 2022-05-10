import ctypes
# Test ctypes.CField
assert ctypes.sizeof(ctypes.CField) == 3 * ctypes.sizeof(ctypes.c_void_p)
# Test ctypes.CField_size
assert ctypes.sizeof(ctypes.CField_size) == ctypes.sizeof(ctypes.c_void_p)
# Test ctypes.CField_offset
assert ctypes.sizeof(ctypes.CField_offset) == ctypes.sizeof(ctypes.c_void_p)
# Test ctypes.CField_index
assert ctypes.sizeof(ctypes.CField_index) == ctypes.sizeof(ctypes.c_void_p)
