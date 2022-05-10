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

for o in [A, B, C, D]:
    print(o, gc.get_referents(o))

print(gc.collect())

for o in [A, B, C, D]:
    print(o, gc.get_referents(o))

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()

print(gc.get_referrers(a))
print(gc.get_referrers(b))
print(gc.get_referrers(c))
print(gc.get_referrers(d))

# Test gc.get_objects()

print(len(gc.get_objects()))

# Test gc.get_stats()

print(gc.get_stats())

# Test gc.is_tracked()
