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

print(s.x.__class__)
print(s.y.__class__)
print(s.z.__class__)

print(s.x.__class__.__class__)
print(s.y.__class__.__class__)
print(s.z.__class__.__class__)

print(s.x.__class__.__class__.__class__)
print(s.y.__class__.__class__.__class__)
print(s.z.__class__.__class__.__class__)

print(s.x.__class__.__class__.__class__.__class__)
print(s.y.__class__.__class__.__class__.__class__)
