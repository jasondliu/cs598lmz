import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S.from_buffer(bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00'))
print(s2.x, s2.y)

s3 = S.from_buffer_copy(bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00'))
print(s3.x, s3.y)

print(s2.x, s2.y)

s4 = S.from_buffer(bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00'))
print(s4.x, s4.y)

s4.x = 3
print(s4.x, s4.y)

