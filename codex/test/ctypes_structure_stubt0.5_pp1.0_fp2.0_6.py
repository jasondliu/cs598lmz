import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32(0)
    y = ctypes.c_uint32(0)
    z = ctypes.c_uint32(0)

s = S()
s.x = 1
s.y = 2
s.z = 3

buf = ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s))
print(buf)

# unpack
s2 = ctypes.cast(ctypes.create_string_buffer(buf, len(buf)), ctypes.POINTER(S)).contents
print(s2.x, s2.y, s2.z)

# pack
buf = ctypes.string_at(ctypes.addressof(s2), ctypes.sizeof(s2))
print(buf)

# unpack
s3 = ctypes.cast(ctypes.create_string_buffer(buf, len(buf)), ctypes.POINTER(S)).contents
print(s3.x, s3.y, s3.z)
