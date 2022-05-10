from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test __repr__
class A:
    def __repr__(self):
        return 'A'

class B(A):
    def __repr__(self):
        return 'B'

class C(A):
    def __repr__(self):
        return 'C'

class D(B, C):
    pass

class E(D):
    pass

class F(E):
    pass

class G(F):
    pass

class H(G):
    pass

class I(H):
    pass

class J(I):
    pass

class K(J):
    pass

class L(K):
    pass

class M(L):
    pass

class N(M):
    pass

class O(N):
    pass

class P(O):
    pass

class Q(P):
    pass

class R(Q):
    pass

class S(R):
    pass

class T(S):

