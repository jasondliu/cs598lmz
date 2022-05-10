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
    b.a = a
    b.c = c
    c.b = b
    d.b = b
    d.c = c
    d.a = a
    b.d = d
    c.d = d
    a.d = d
    del a, b, c, d
    gc.collect()

f()
f()
f()
f()

# Test gc.get_referents()

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
    a
