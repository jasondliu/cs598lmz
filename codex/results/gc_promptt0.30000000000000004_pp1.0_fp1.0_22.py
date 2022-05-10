import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        self.c = C(self)
        self.d = D(self)
        self.e = E(self)
        self.f = F(self)
        self.g = G(self)
        self.h = H(self)
        self.i = I(self)
        self.j = J(self)

class B:
    def __init__(self, a):
        self.a = a

class C:
    def __init__(self, a):
        self.a = a

class D:
    def __init__(self, a):
        self.a = a

class E:
    def __init__(self, a):
        self.a = a

class F:
    def __init__(self, a):
        self.a = a

class G:
    def __init__(self, a):
        self.a = a

class H:
    def __init__(
