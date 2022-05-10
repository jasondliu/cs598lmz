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
    a.x = c
    a.y = c
    a.z = c
    a.t = c

gc.collect()

# Test gc.get_referrers()

a = A()
a.x = A
a.y = A
a.z = A
a.t = A

gc.collect()

# Test gc.get_referents()

a = A()
a.x = A
a.y = A
a.z = A
a.t = A

gc.collect()

# Test gc.get_objects()

a = A()
a.x = A
a.y = A
a.z = A
a.t = A

gc.collect()

# Test gc.is_tracked()

a
