import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

s.x = ctypes.c_int(3)
s.y = ctypes.c_int(4)

print(s.x, s.y)

s.x = 5
s.y = 6

print(s.x, s.y)

s.x = ctypes.c_int(7)
s.y = ctypes.c_int(8)

print(s.x, s.y)
