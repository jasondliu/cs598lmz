import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C(object):
    pass

def f():
    c = C()
    wr = weakref.ref(c)
    del c
    gc.collect()
    return wr

wr = f()
assert wr() is None

# Test gc.collect() with uncollectable objects.

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(object):
    def __init__(self, x=None):
        self.x = x

class F(E):
    pass

gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
a = A()
b = B()
c = C()
d = D()
e = E()
f = F()

a.b = b
a.c = c
a.d = d
a.e = e
a.f = f

b.a = a
b.c = c
