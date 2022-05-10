import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(S.x)
print(S.x.__class__)
print(ctypes.CField)

assert type(S.x) is ctypes.CField
</code>

