import ctypes
# Test ctypes.CFUNCTYPE
assert ctypes.CFUNCTYPE(None)(lambda: None)
# Test ctypes.c_bool
assert ctypes.c_bool(1)
# Test ctypes.c_size_t
assert ctypes.c_size_t(1)
# Test ctypes.c_ssize_t
assert ctypes.c_ssize_t(1)
# Test ctypes.c_int8
assert ctypes.c_int8(1)
# Test ctypes.c_uint8
assert ctypes.c_uint8(1)
# Test ctypes.c_int16
assert ctypes.c_int16(1)
# Test ctypes.c_uint16
assert ctypes.c_uint16(1)
# Test ctypes.c_int32
assert ctypes.c_int32(1)
# Test ctypes.c_uint32
assert ctypes.c_uint32(1)
# Test ctypes.c_int64
assert ctypes.c_int64(1)
# Test ctypes.c_uint64
assert ctypes
