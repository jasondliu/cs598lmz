import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class SubField(ctypes.CField):
    pass

f = SubField(ctypes.c_int, 'x')

s = S()
assert type(s.x) is SubField
</code>
This is not very straightforward, but is the best I can do.

