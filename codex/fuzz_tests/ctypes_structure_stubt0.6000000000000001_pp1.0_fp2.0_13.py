import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S(x=1)
print s.x
s.x = 2
print s.x
</code>

