import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    a = 1
    b = 2

    def __init__(self, x):
        self.x = x

class B(A):
    y = 3

class C(B):
    z = 4

class D(C):
    z = 5

class E(D):
    z = 6

class F(E):
    z = 7

class G(F):
    z = 8

class H(G):
    z = 9

class I(H):
    z = 10

class J(I):
    z = 11

class K(J):
    z = 12

class L(K):
    z = 13

class M(L):
    z = 14

class N(M):
    z = 15

class O(N):
    z = 16

class P(O):
    z = 17

class Q(P):
    z = 18

class R(Q):
    z = 19

class S(R):
    z = 20

class T
