import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', S),
        ('w', ctypes.c_int)
    ]

S._fields_.insert(2, ('y', ctypes.c_int))
print(S.x)
print(S.y)
print(S.z)
print(S.w)
print(S.x.offset)
print(S.y.offset)
print(S.z.offset)
print(S.w.offset)

print(type(S.x))
print(type(S.y))
print(type(S.z))
print(type(S.w))
</code>

