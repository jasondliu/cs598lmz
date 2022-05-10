import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

s = S()
c = C(s)

print(c.s.x)
print(c.s.x.__class__)
print(c.s.x.__class__ == ctypes.CField)

print(c.s.x.value)
print(c.s.x.value.__class__)
print(c.s.x.value.__class__ == int)

print(c.s.x.value == c.s.x)
print(c.s.x.value == c.s.x.value)

c.s.x = 4
print(c.s.x.value)
print(c.s.x.value == c.s.x)

c.s.x = c.s.x.value
print(c.s.x.value)
print(c.s.x.value == c.s.x)

c.s.x = ctypes.c_int(4
