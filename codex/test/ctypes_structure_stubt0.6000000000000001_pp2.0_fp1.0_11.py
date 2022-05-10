import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(0)
    y = ctypes.c_ulong(1)
    z = ctypes.c_ulong(2)
    w = ctypes.c_ulong(3)

s = S()

print(s.x)
print(s.y)
print(s.z)
print(s.w)

s.x = 5
s.y = 6
s.z = 7
s.w = 8

print(s.x)
print(s.y)
print(s.z)
print(s.w)
