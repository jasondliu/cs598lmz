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
class F(D, E):
    pass
gc.collect()
# Test gc.get_objects()
gc.get_objects()
# Test gc.get_referrers()
gc.get_referrers(A)
gc.get_referrers(B)
gc.get_referrers(C)
gc.get_referrers(D)
gc.get_referrers(E)
gc.get_referrers(F)
gc.get_referrers(gc.get_objects)
# Test gc.get_referents()
gc.get_referents(A)
gc.get_referents(B)
gc.get_referents(C)
gc.get_referents(D)
gc.get_referents(E)
gc.get_referents(F)
gc.get_referent
