import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16(1)
    y = ctypes.c_int16(2)

s = S.from_buffer(bytearray(b"\x01\x00\x02\x00"))
print(s.x, s.y)
</code>

