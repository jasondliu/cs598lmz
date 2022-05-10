import weakref
# Test weakref.ref
import unittest
from test import test_support

class MyBase:
    pass

class MyKlass(MyBase):
    pass

class MyInt(int):
    pass

class MyInt2(int):
    def __hash__(self):
        return int.__hash__(self)

class C:
    pass

class D(C):
    pass

class E(C):
    pass

class F(D, E):
    pass

class G(F):
    pass

class H(object):
    pass

class I(H):
    pass

class J(H):
    pass

class K(I, J):
    pass

class L(K):
    pass

class M(object):
    pass

class N(M):
    pass

class O(M):
    pass

class P(N, O):
    pass

class Q(P):
    pass

class R(object):
    pass

class S(R):
    pass

class T(R):
