import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        self.c = C(self)
        self.d = D(self)

class B:
    def __init__(self, a):
        self.a = a

class C:
    def __init__(self, a):
        self.a = a

class D:
    def __init__(self, a):
        self.a = weakref.ref(a)

a = A()
del a
gc.collect()

# Test gc.get_referrers()

class A:
    pass

a = A()
l = [a]
d = {1: a}

gc.get_referrers(a) == [l, d]

# Test gc.get_referents()

gc.get_referents(l) == [a]
gc.get_referents(d) == [a]

# Test gc.get_objects()

# XXX This test is
