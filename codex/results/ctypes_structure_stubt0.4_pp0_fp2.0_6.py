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

s.x = 1
s.y = 2
s.z = 3

s2 = S(1, 2, 3)

print(s2.x, s2.y, s2.z)

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

s.x = 1
s.y = 2
s.z = 3

s2 = S(x=1, y=2, z=3)

print(s2.x, s2.y, s2.z)

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

