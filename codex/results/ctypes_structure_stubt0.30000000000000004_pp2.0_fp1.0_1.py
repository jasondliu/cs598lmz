import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

print(S.x)
print(S.y)
print(S._fields_)

s = S()
print(s.x)
print(s.y)

s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s)
print(s.__dict__)
print(s.__class__)
print(s.__class__.__dict__)
print(s.__class__._fields_)
print(s.__class__.__bases__)
print(s.__class__.__bases__[0].__dict__)
print(s.__class__.__bases__[0].__bases__)
print(s.__class__.__bases__[0].__bases__[0].__dict__)
print(s.__class__
