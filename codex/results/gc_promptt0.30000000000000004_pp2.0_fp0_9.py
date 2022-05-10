import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    wr = weakref.ref(x)
    del x
    return wr

wr = f()
gc.collect()
print wr()

# Test gc.garbage

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

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    a.b = b
    b.a = a
    b.c = c
    c.b = b
    c.d = d
    d.c = c
    d.a = a
    a.d = d
    e.a = a
    a.e = e
    del a, b, c, d, e

f()
gc.collect()
print gc.garbage

# Test
