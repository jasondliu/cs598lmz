import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

s = S()
s.x = 1.0
s.y = 2.0
s.z = 3.0

print s.x, s.y, s.z
</code>
This prints <code>1.0 2.0 3.0</code>

