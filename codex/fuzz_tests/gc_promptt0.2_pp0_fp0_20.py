import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_referrers()
class A:
    pass

class B(A):
    pass

class C(A):
    pass

a = A()
b = B()
c = C()

print(gc.get_referrers(A))
print(gc.get_referrers(B))
print(gc.get_referrers(C))
print(gc.get_referrers(a))
print(gc.get_referrers(b))
print(gc.get_referrers(c))

# Test gc.get_referents()
print(gc.get_referents(a))
print(gc.get_referents(b))
print(gc.get_referents(c))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_stats()
print(gc.get_stats())

# Test gc.is_tracked()
print(gc.is_tracked(
