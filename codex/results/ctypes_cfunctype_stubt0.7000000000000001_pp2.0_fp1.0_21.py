import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(1)

class A(object):
    _as_parameter_ = None

class B(A):
    _as_parameter_ = None

class C(B):
    _as_parameter_ = None

class D(C):
    _as_parameter_ = None

class E(D):
    _as_parameter_ = None

class F(E):
    _as_parameter_ = None

class G(F):
    _as_parameter_ = None

class H(G):
    _as_parameter_ = None

class I(H):
    _as_parameter_ = None

class J(I):
    _as_parameter_ = None

class K(J):
    _as_parameter_ = None

class L(K):
    _as_parameter_ = None

class M(L):
    _as_parameter_ = None

class N(M):
    _as_parameter_ = None

class O(N
