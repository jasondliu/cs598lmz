import ctypes
# Test ctypes.CFUNCTYPE
def py_callback(x):
    return x + 1
callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(py_callback)
assert callback(2) == 3
# Test ctypes.POINTER
c_pointer = ctypes.POINTER(ctypes.c_int)
assert c_pointer(ctypes.c_int(10)).contents.value == 10
# Test ctypes.c_int32
assert ctypes.c_int32(10).value == 10
# Test ctypes.c_int64
assert ctypes.c_int64(10).value == 10
# Test ctypes.c_uint32
assert ctypes.c_uint32(10).value == 10
# Test ctypes.c_uint64
assert ctypes.c_uint64(10).value == 10
# Test ctypes.c_float
assert ctypes.c_float(10.5).value == 10.5
# Test ctypes.c_double
assert ctypes.c_double(10.5).value == 10.5
#
