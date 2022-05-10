import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
print s.x, s.y

del s.x
print s.x

s.x = 3
print s.x, s.y
