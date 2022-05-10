import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('d', ctypes.c_double)]

s = S()
c = C()

# test ctypes fields are ctypes types
assert issubclass(c.x, ctypes.CField)
assert issubclass(c.x, ctypes._CData)
assert not issubclass(c.x, ctypes.Structure)

c.x = ctypes.c_int
assert c.x is ctypes.c_int

c.x = ctypes.c_double
assert c.x is ctypes.c_double

c.x = ctypes.c_longlong
assert c.x is ctypes.c_longlong

c.x = d = D.d
assert c.x is d

try:
    c.x = s.x
except TypeError:
    pass
else:
    assert False

try:
    c.x
