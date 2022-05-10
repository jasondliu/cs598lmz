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

class E:
    pass

for o in [A, B, C, D, E]:
    o.attr = A()

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    a.b = b
    a.c = c
    a.d = d
    a.e = e
    b.a = a
    b.c = c
    b.d = d
    b.e = e
    c.a = a
    c.b = b
    c.d = d
    c.e = e
    d.a = a
    d.b = b
    d.c = c
    d.e = e
    e.a = a
    e.b = b
    e.c = c
    e.d = d
    return a, b,
