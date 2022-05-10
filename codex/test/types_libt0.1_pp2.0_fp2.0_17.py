import types
types.MethodType(lambda self: None, None, None)

# classes
class A:
    pass

class B(A):
    pass

class C(A, B):
    pass

class D(A, B, C):
    pass

class E(A, B, C, D):
    pass

class F(A, B, C, D, E):
    pass

class G(A, B, C, D, E, F):
    pass

class H(A, B, C, D, E, F, G):
    pass

class I(A, B, C, D, E, F, G, H):
    pass

class J(A, B, C, D, E, F, G, H, I):
    pass

class K(A, B, C, D, E, F, G, H, I, J):
    pass
