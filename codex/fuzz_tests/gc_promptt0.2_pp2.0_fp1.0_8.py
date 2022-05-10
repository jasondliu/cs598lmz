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
    a = None
    gc.collect()
    print gc.collect()

# Test gc.get_objects()

class G:
    pass

gc.collect()
l = gc.get_objects()
before = len(l)
a = G()
gc.collect()
l = gc.get_objects()
after = len(l)
print after - before

# Test gc.get_referrers()

class H:
    pass

gc.collect()
l = gc.get_referrers(H)
before = len(l)
a = H()
gc.collect()
l = gc.get_referrers(H)
after = len(l)
print after - before

# Test gc
