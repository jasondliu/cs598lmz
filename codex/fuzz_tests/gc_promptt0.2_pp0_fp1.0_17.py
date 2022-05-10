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
    l = [a, b, c, d]
    del a, b, c, d
    return l

def g():
    a = A()
    b = B()
    c = C()
    d = D()
    l = [a, b, c, d]
    del a, b, c, d
    return l

def h():
    a = A()
    b = B()
    c = C()
    d = D()
    l = [a, b, c, d]
    del a, b, c, d
    return l

def i():
    a = A()
    b = B()
    c = C()
    d = D()
    l = [a, b, c, d]
    del a
