import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(X):
    _fields_ = [("y", ctypes.c_int)]

class Z(Y):
    _fields_ = [("z", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class B(A):
    _fields_ = [("b", ctypes.c_int)]

class C(B):
    _fields_ = [("c", ctypes.c_int)]

class D(C):
    _fields_ = [("d", ctypes.c_int)]

class E(D):
    _fields_ = [("e", ctypes.c_int)]

class F(E):
    _fields_ = [("f", ctypes.c_int)]

class G(F):
    _fields_ = [("g", ctypes.c_int)]

class H(G):
   
