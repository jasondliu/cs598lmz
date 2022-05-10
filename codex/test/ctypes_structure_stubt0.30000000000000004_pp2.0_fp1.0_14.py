import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long
    y = ctypes.c_long

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s)

print(ctypes.sizeof(S))
print(ctypes.sizeof(s))

print(ctypes.addressof(s))
