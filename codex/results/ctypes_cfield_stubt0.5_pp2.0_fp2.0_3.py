import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print C.x.__class__
print D.x.__class__
print E.x.__class__

print C.x
print D.x
print E.x

print C.x == D.x
print C.x == E.x
print D.x == E.x

print C.x is D.x
print C.x is E.x
print D.x is E.x
