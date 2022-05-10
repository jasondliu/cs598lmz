import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class G(E, F):
    _fields_ = [('y', ctypes.c_int)]

class H(G):
    _fields_ = [('z', ctypes.c_int)]

class I(H):
    _fields_ = [('w', ctypes.c_int)]

class J(G):
    _fields_ = [('y', ctypes.c_int)]

print(E.__mro__)
print(G.__mro__)
print(H.__mro__)
print(I.__mro__)
print(J
