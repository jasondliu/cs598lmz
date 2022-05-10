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

s.y = 4

print(s.x, s.y, s.z)

s.y = 5

print(s.x, s.y, s.z)
