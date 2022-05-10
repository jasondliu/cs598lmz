import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s2 = S.from_buffer_copy(s)
s2.x = 3

print(s.x, s.y)
print(s2.x, s2.y)

