import ctypes

class S(ctypes.Structure):
    x = P(a=1, b=2, c=3)
    _fields_ = [("x", P)]

s = S()
print(s.x.a, s.x.b, s.x.c)
print(s.x.d)
</code>

