import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()
print(s.x, s.y)
s.x = 42
print(s.x, s.y)
s.y = 42
print(s.x, s.y)
</code>
Output:
<code>1 2
42 2
42 42
</code>

