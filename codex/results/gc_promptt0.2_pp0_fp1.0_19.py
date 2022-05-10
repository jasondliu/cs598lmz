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

class E(A):
    pass

class F(D, E):
    pass

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    f = F()
    l = [a, b, c, d, e, f]
    wr = weakref.ref(f)
    del f
    return wr

wr = f()
gc.collect()
print wr() is None
