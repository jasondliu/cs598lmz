import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 42
s.y = 0

print(s.x)
print(s.y)

print(s.x.__class__)
print(s.y.__class__)

