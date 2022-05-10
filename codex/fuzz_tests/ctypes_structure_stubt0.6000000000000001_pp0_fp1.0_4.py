import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int)]

s = S()
print s.x
s.x = 42
print s.x
</code>

