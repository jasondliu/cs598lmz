import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(s):
    s.x = 1
    s.y = 2
    s.z = 3

s = S()
f(s)
print s.x, s.y, s.z
</code>
Output:
<code>1 2 3
</code>

