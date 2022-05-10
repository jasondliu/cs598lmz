import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    pass

class E(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class F(D, E):
    pass

class G(F):
    _fields_ = [('z', ctypes.c_int)]

class H(G):
    pass

print(H.x)
print(H.y)
print(H.z)
