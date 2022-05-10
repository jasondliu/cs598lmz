import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()

s.x = 2
s.y = 3

print s.x
print s.y
</code>

