import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    l = [a, b, c, d, e]
    del a, b, c, d, e
    return l

def g():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    l = [a, b, c, d, e]
    del a, b, c, d, e
    return l

def h():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    l = [a,
