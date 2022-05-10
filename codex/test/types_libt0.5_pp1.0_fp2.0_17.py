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

