import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(3)

s = S()
print s.x
s.x = 4
print s.x

class S2(ctypes.Structure):
    x = ctypes.c_int

s2 = S2(3)
print s2.x
s2.x = 4
print s2.x
</code>

