import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    a.b = b
    a.c = c
    a.d = d
    b.a = a
    b.c = c
    b.d = d
    c.a = a
    c.b = b
    c.d = d
    d.a = a
    d.b = b
    d.c = c
    return a, b, c, d

gc.collect()
a, b, c, d = f()
gc.collect()

# Test gc.get_referents()

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    a.b = b
    a.c = c
    a.d = d
    b.a =
