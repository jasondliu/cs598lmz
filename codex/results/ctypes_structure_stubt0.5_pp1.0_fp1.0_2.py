import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    w = ctypes.c_double

s = S(1,2,3,4)
print s.x
s.x = 5
print s.x
</code>
Output:
<code>1.0
5.0
</code>

