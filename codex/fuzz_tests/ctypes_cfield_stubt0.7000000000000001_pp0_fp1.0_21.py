import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
and then you can use CField's in the field spec:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.CField * 4)]

s = S()
s.x[0] = 1
s.x[1] = 2
print s.x[0], s.x[1]
</code>

