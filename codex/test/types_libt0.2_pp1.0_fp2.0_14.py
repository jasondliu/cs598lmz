import types
types.MethodType(lambda self: self.x, None, A)

class B(A):
    pass

B.f = types.MethodType(lambda self: self.x, None, B)

class C(A):
    def f(self):
        return self.x

class D(B, C):
    pass

D.f = types.MethodType(lambda self: self.x, None, D)

class E(D):
    pass

E.f = types.MethodType(lambda self: self.x, None, E)

class F(E):
    pass

F.f = types.MethodType(lambda self: self.x, None, F)
