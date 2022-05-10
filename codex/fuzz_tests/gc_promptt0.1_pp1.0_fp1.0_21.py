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
    a = None
    gc.collect()
    print gc.garbage
    del gc.garbage[:]

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
    l = gc.get_referrers(a)
    print l
    del l
    a = None
    gc.collect()

# Test gc.get_referents()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

for
