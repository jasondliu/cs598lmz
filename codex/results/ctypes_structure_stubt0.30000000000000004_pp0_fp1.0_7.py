import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S(1, 2, 3)
print(s.x, s.y, s.z)

s.x = 4
print(s.x, s.y, s.z)

s.y = 5
print(s.x, s.y, s.z)

s.z = 6
print(s.x, s.y, s.z)

s.x = 7
print(s.x, s.y, s.z)

s.y = 8
print(s.x, s.y, s.z)

s.z = 9
print(s.x, s.y, s.z)

s.x = 10
print(s.x, s.y, s.z)

s.y = 11
print(s.x, s.y, s.z)

s.z = 12
print(s.x, s.y, s.z)

s.
