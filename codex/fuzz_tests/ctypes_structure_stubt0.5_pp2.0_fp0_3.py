import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool
    y = ctypes.c_bool
    _fields_ = [('x', ctypes.c_bool), ('y', ctypes.c_bool)]

s = S()
print s.x, s.y
s.x = True
print s.x, s.y
s.y = True
print s.x, s.y
</code>
Output:
<code>False False
True False
True True
</code>

