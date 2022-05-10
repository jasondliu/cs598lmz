import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

a = A()
w = weakref.ref(a)

gc.collect()

print gc.get_referrers(a)
print gc.get_referrers(w)
print gc.get_referrers(w())

del a
gc.collect()

print gc.get_referrers(w)
print gc.get_referrers(w())

del w
gc.collect()

print gc.get_referrers(w)
print gc.get_referrers(w())
