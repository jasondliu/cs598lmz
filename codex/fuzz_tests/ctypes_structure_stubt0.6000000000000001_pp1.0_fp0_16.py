import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

#s = S()
#s.x = 1.0
#s.y = 2.0

s = S(1.0, 2.0)
print s.x
print s.y

s = S(1.0, y=2.0)
print s.x
print s.y
</code>

