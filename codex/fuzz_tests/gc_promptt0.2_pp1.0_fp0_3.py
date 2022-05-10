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
    print gc.collect()

# Test gc.get_referrers()

class A:
    pass

a = A()
print gc.get_referrers(a)

# Test gc.get_referents()

class A:
    pass

a = A()
print gc.get_referents(a)

# Test gc.get_objects()

class A:
    pass

a = A()
print gc.get_objects()

# Test gc.is_tracked()

class A:
    pass

a = A()
print gc.is_tracked(a)

# Test gc.is_finalized()

class A:
    pass


