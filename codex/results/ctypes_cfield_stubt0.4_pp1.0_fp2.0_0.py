import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [('f', ctypes.CField)]

print C.f
print C.f.__class__
print C.f.__class__.__bases__
print C.f.__class__.__bases__[0]
print C.f.__class__.__bases__[0].__bases__
print C.f.__class__.__bases__[0].__bases__[0]
print C.f.__class__.__bases__[0].__bases__[0].__bases__
print C.f.__class__.__bases__[0].__bases__[0].__bases__[0]
print C.f.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__
print C.f.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0]

