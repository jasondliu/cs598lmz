import types
types.MethodType(lambda self: None, None, None)

# classes
class A:
    pass

class B(A):
    pass

class C(A, B):
    pass

class D(C, B):
    pass

class E(D, C):
    pass

class F(E, D):
    pass

class G(F, E):
    pass

class H(G, F):
    pass

class I(H, G):
    pass

class J(I, H):
    pass

class K(J, I):
    pass

class L(K, J):
    pass

class M(L, K):
    pass

class N(M, L):
    pass

class O(N, M):
    pass

class P(O, N):
    pass

class Q(P, O):
    pass

class R(Q, P):
    pass

class S(R, Q):
    pass

class T(S, R):
    pass
