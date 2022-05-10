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
    for i in range(2):
        x = c()
        x.a = c()
        x.a.b = x

del x
gc.collect()

# Test gc.get_referrers()

a = A()
a.b = A()
a.b.a = a

del a
gc.collect()

# Test gc.get_referents()

a = A()
a.b = A()
a.b.a = a

del a
gc.collect()

# Test gc.is_tracked()

a = A()
a.b = A()
a.b.a = a

del a
gc.collect()

# Test gc.get_objects()

a = A()
a.b = A()
a.b.a =
