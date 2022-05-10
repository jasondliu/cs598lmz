import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Union):
    _fields_ = [('u', S), ('x', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('u', X)]

y = Y()
y.u.u.x = 42
print y.u.x
try:
    y.u.x = 42
except TypeError, details:
    print details

print type(y.u)
print type(y.u.x)
print type(y.u.u)
print type(y.u.u.x)
print type(y.u.u.x) == ctypes.c_int
print type(y.u.u.x) == ctypes.CField

class Z(ctypes.Structure):
    _fields_ = [('u', S)]

z = Z()
z.u.x = 42
try:
    z.u.x = 42
except TypeError, details:
    print details

print type(z.u)
print type(z.u
