import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C(object):
    pass

def f():
    c = C()
    wr = weakref.ref(c)
    del c
    return wr

wr = f()
gc.collect()

print wr() is None
print wr() is None

# Test gc.garbage

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(A):
    pass

class E(B, C):
    pass

class F(D, E):
    pass

def create_cycle():
    a = A()
    a.b = B()
    a.b.a = a
    a.b.c = C()
    a.b.c.b = a.b
    a.d = D()
    a.d.b = a.b
    a.d.e = E()
    a.d.e.a = a
    a.d.e.b = a.b
    a.d.e.c = a
