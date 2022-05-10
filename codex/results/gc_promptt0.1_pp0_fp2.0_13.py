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

for c in [A, B, C, D, E]:
    a = c()
    a.x = c
    a.y = weakref.ref(a)
    a.z = weakref.ref(a)
    del a

gc.collect()

# Test gc.get_referrers()

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

for c in [A, B, C, D, E]:
    a = c()
    a.x = c
    a.y = weakref.ref(a)
    a.z = weakref.ref(a)
    del a

gc.collect()

# Test gc.get_referents()


