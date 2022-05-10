import types
types.MethodType(lambda self: None, None)

# tests for __subclasses__()

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(B):
    pass

class F(E):
    pass

class G(D, F):
    pass

