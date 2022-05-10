import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_float
    z = ctypes.c_int

s = S()
s.z = -1
s.x = 1.0
s.y = 2.0

print s.z, s.x, s.y
</code>
Output:
<code>-1 1.0 2.0
</code>

