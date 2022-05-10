import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 2
s.y = 3

print s.x * s.y
print s.y * s.x
</code>

