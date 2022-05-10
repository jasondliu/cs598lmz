import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()

class T(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()

def f(s):
    print s.x, s.y, s.z

s = S(x=1.0, y=2.0, z=3.0)
t = T(x=1, y=2, z=3)

f(s)
f(t)
</code>
The output is:
<code>1.0 2.0 3.0
1 2 3
</code>
This is much simpler than writing separate functions for each structure.

