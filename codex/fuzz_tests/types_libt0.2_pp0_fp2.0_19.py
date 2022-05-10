import types
types.MethodType(lambda self: None, None, None)

# classes
class A(object):
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        pass

class C(A):
    def __init__(self):
        pass

class D(B, C):
    def __init__(self):
        pass

class E(object):
    def __init__(self):
        pass

class F(E):
    def __init__(self):
        pass

class G(E):
    def __init__(self):
        pass

class H(F, G):
    def __init__(self):
        pass

class I(object):
    def __init__(self):
        pass

class J(I):
    def __init__(self):
        pass

class K(I):
    def __init__(self):
        pass

class L(J, K):
    def __init__(self):
        pass

class M(object
