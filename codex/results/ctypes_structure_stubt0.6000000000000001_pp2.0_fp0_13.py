import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int


s = S()
print(s.x)
print(s.y)
print(s.z)
print(s.a)

print(s.x.__class__)
print(s.y.__class__)
print(s.z.__class__)
print(s.a.__class__)
