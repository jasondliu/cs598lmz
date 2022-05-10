import types
types.MethodType(lambda self: None, None, None)

# classes
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class F(E):
    def __init__(self, a, b, c, d):
        E.__init__(self, a, b, c)
        self.d = d

class G(E):
    def __init__(self, a, b, c, d):
        E.__init__(self, a, b, c)
        self.d = d

