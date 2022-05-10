import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(ctypes.CField)
print(type(ctypes.CField))

for t in [int, ctypes.c_int, S.x]:
    print(t, issubclass(type(t), ctypes.CField))
</code>

