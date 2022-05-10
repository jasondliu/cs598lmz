import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = (('x', ctypes.c_int), ('y', ctypes.c_int))

s = S(1, 2)
print s.x, s.y
s.x = 3
print s.x, s.y

s.y = 4
print s.x, s.y
</code>
outputs
<code>1 2
3 2
3 4
</code>

