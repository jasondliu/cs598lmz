import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 2
s.y = 3

print s.x, s.y

s = S(1, 2)
print s.x, s.y

s = S(y=2, x=1)
print s.x, s.y

s = S(2)
print s.x, s.y
