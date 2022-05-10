import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)
    y = ctypes.c_double(2.0)
    z = ctypes.c_double(3.0)

s = S()
print(s.x, s.y, s.z)

s.x = 1.0
s.y = 2.0
s.z = 3.0
print(s.x, s.y, s.z)

s.x = 1.0
s.y = 2.0
s.z = 3.0
print(s.x, s.y, s.z)

s.x = 1.0
s.y = 2.0
s.z = 3.0
print(s.x, s.y, s.z)

s.x = 1.0
s.y = 2.0
s.z = 3.0
print(s.x, s.y, s.z)

s.x = 1.0
s.y = 2.0
s.z = 3.0
print(s.x, s
