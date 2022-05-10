import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char), ('s', S)]


x = X()
print(x.s.x)
x.s.x = 5
print(x.s.x)
x.s.x = 12
print(x.s.x)
print(x.s)
print(x.s.__class__)
print(x.s.x.__class__)
print(x.c)
print(x.__class__)
print(x.__dict__)
print(x.s.__dict__)
print(dir(x.s))
print(dir(x.s.x))
print(dir(x))
print(hasattr(x.s, 'x'))
print(hasattr(x.s, 'y'))

S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_float)]
print(x.s.x)
print(x.s.y)

print(X
