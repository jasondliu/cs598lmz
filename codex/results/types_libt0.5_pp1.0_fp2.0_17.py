import types
types.MethodType(f, None, B)

class C(object):
    def f(self):
        pass

class D(C):
    pass

D.f.__func__.__class__

def f(self):
    pass

class E(object):
    pass

C.f = f

class F(C):
    pass

F.f(F())

types.MethodType(f, None, E)

class G(object):
    pass

types.MethodType(f, None, G)

class H(object):
    def f(self):
        pass

class I(H):
    pass

I.f

class J(I):
    pass

J.f

J.f.__func__.__class__

J.f.__func__.__class__ = type

class K(object):
    def __get__(self, ob, type=None):
        return self

class L(object):
    f = K()

L.f

class M(L
