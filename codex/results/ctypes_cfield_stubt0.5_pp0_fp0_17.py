import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

c = C()
print(type(c.s))
print(type(c.s.x))

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('s', S)]

d = D()
print(type(d.s))
print(type(d.s.x))

import _ctypes
print(type(S.x))
print(type(_ctypes.Structure))
print(type(ctypes.Structure))
print(type(ctypes.Union))
print(type(ctypes.PyCArrayType))
print(type(ctypes.CFuncPtr))
print(type(ctypes.CField))
</code>

