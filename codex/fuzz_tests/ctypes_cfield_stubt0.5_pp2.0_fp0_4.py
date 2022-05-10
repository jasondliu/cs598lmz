import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('a', X),
                ('b', Y)]

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class U(ctypes.Union):
    _fields_ = [('t', T),
                ('z', Z)]

class V(ctypes.Structure):
    _fields_ = [('u', U),
                ('w', ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [('v', V)]

print(W.v.u.t.x)
print(W.v.u.t.y)
print(
