import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(3)


s = S()
print s.x
s.x = 4
print s.x
</code>

