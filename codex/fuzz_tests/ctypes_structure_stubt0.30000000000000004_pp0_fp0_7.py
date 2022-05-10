import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s.x = 3
s.y = 4

print s.x, s.y
</code>

