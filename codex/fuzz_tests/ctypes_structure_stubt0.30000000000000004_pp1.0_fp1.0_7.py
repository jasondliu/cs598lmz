import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

s2 = S(1, 2, 3)

print(s2.x, s2.y, s2.z)

s3 = S(x=1, y=2, z=3)

print(s3.x, s3.y, s3.z)

s4 = S(y=2, x=1, z=3)

print(s4.x, s4.y, s4.z)
