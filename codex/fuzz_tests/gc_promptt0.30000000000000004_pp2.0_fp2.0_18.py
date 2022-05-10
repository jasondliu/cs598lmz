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

for c in [A, B, C, D]:
    a = c()
    a.foo = a
    wr = weakref.ref(a)
    del a
    gc.collect()
    assert wr() is None

# Test gc.get_referrers()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

for c in [A, B, C, D]:
    a = c()
    a.foo = a
    l = gc.get_referrers(a)
    assert len(l) == 2
    assert a in l
    assert l[1] is l
    del a
    gc.collect()

# Test gc.get_referents()

class A:
    pass

class B(A):
