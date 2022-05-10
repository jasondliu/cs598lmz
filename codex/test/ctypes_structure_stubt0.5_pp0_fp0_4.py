import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
print(s.y)

s.x = 1
s.y = 2
print(s.x)
print(s.y)

print(ctypes.sizeof(s))
