import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S(1, 2, 3)
print s.x
print s.y
print s.z

s.x = 4
print s.x
print s.y
print s.z

s.y = 5
print s.x
print s.y
print s.z

s.z = 6
print s.x
print s.y
print s.z
