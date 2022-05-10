import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(isinstance(S.x, ctypes.CField))

d = {S.x: 1}
print(d)
</code>

