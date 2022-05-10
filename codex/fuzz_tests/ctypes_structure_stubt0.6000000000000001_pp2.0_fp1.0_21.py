import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print(type(s))

print(type(s.x))
print(type(s.y))
print(type(s.z))

print(s.x)
print(s.y)
print(s.z)
