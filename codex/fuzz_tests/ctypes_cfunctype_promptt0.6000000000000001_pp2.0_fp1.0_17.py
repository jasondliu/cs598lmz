import ctypes
# Test ctypes.CFUNCTYPE
def cb(a,b):
    return a+b

cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(cb)
assert cb_p(1, 2) == 3

# Test ctypes.byref
p = ctypes.c_int(1)
assert ctypes.byref(p).contents.value == 1

# Test ctypes.string_at
assert ctypes.string_at(ctypes.byref(p), 4) == b'\x01\x00\x00\x00'

# Test ctypes.memmove
p1 = ctypes.c_char_p(b'\x01\x02\x03')
p2 = ctypes.c_char_p(b'\x04\x05\x06')
ctypes.memmove(ctypes.byref(p1), p2, 3)
assert p1.value == b'\x04\x05\x06'

# Test ctypes.cast
