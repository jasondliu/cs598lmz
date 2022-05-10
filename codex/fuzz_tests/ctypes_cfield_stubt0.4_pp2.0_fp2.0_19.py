import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    pass

X._fields_ = [('y', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('x', X)]

print(type(Y.x))
print(type(Y.x.y))
print(type(Y.x.y.__class__))
print(type(Y.x.y.__class__.__class__))
print(type(Y.x.y.__class__.__class__.__class__))
print(type(Y.x.y.__class__.__class__.__class__.__class__))
print(type(Y.x.y.__class__.__class__.__class__.__class__.__class__))
print(type(Y.x.y.__class__.__class__.__class__.__class__.__class__.__class__))
print(type(Y.x.y.__class__.__class__.__class__.__class__.__class
