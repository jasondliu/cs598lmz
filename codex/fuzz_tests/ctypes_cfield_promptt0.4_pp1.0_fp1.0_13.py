import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

class E(C):
    _fields_ = [("c", ctypes.c_int)]

class F(D, E):
    _fields_ = [("d", ctypes.c_int)]

class G(F):
    _fields_ = [("e", ctypes.c_int)]

# Test ctypes.CField
class H(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class I(H):
    _fields_ = [("c", ctypes.c_int)]

class J(H):
    _fields_ = [("c", ctypes.c_int)]

class K(I, J):
    _fields_ = [("d", ctypes.c
