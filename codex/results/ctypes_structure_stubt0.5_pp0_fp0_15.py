import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32

class T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]

s = S(1, 2)
t = T(1, 2)

print(s.x)
print(t.x)

print(s.y)
print(t.y)

print('=' * 20)

print(s)
print(t)

print(s.__dict__)
print(t.__dict__)

print(s.__class__)
print(t.__class__)

print(s.__class__.__name__)
print(t.__class__.__name__)

print(s.__class__.__mro__)
print(t.__class__.__mro__)

print(s.__class__.__module__)
print(t.__class__.__module__)

