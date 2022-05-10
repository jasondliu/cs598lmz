import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class T(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class U(ctypes.Union):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class V(ctypes.Union):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class W(T, S, U, V):
    pass

class X(T, V, S, U):
    pass

class Y(T, U, S, V):
    pass

class Z(T, U, V, S):
    pass

print W.x, S.x, T.x, U.x, V.x
print X.x, S.x, T.x, U.x, V.x
print Y.x, S.x, T.x, U.x, V.x
print Z.x, S.x, T.
