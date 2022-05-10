import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass
C._fields_ = [('a', ctypes.c_int),
              ('b', ctypes.CField)]

s = S()
s.x = 42
c = C()
c.a = s.x
c.b = s.x
assert c.a == c.b

try:
    c = C()
    c.a = c.b
except TypeError:
    pass
else:
    raise RuntimeError

#__test__ = {'type_fields': '''
#>>> from ctypes import *
#>>> class X(Structure):
#...     _fields_ = [("a", c_int),
#...                 ("b", c_int)]
#...
#>>> class Y(Structure):
#...     _fields_ = [("a", c_int),
#...                 ("b", c_int),
#...                 ("c", c_int),
#...                 ("d", X)]
#...
#>>> class Z(Structure):
#...     _fields
