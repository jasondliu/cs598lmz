import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Base(object):
    __slots__ = ()

class A(Base):
    __slots__ = ('a',)

class B(Base):
    __slots__ = ('b',)

class C(A, B):
    __slots__ = ()

class D(C):
    pass

class E(D):
    __slots__ = ('e',)

class F(E):
    __slots__ = ('f',)

class G(F):
    __slots__ = ('g', 'h', 'j')

class H(object):
    __slots__ = ('a', 'b')

class I(H):
    __slots__ = ('c',)

class J(H):
    __slots__ = ('d',)

class K(I, J):
    pass

class L(K):
    __slots__ = ('e',)

class M(object):
    __slots__ = ('a', 'b')

    def __init__(self):
        self
