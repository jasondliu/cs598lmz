import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.POINTER(S)),
                ('a', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('f', ctypes.POINTER(S)),
                ('a', ctypes.c_int)]

s = S(42)
c = C(s, 0)

print(c.f)
print(c.a)
print(c.f.contents)
print(c.f.contents.x)

c.f = cast(c_void_p(id(s)), POINTER(S))
print(c.f.contents.x)

d = D(s, 0)
print(d.f)
print(d.a)
print(d.f.contents)
print(d.f.contents.x)

d.f = cast(c_void_p(id(s)), POINTER(S))
print(d.f.contents.x)
