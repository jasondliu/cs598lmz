import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(s):
    s.x = 1
    s.y = 2
    return s

s = S()
f(s)
print s.x, s.y
</code>
This prints <code>1 2</code> as expected.

