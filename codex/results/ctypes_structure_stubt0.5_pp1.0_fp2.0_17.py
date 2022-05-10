import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print(s.x, s.y)

s.x += 1
print(s.x, s.y)

s.y += 1
print(s.x, s.y)

s.x += 1
print(s.x, s.y)
