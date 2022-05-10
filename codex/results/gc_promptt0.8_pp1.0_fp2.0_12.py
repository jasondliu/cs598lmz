import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class foo:
    pass

f = foo()
w = weakref.ref(f)
print gc.collectable()
print gc.is_tracked(f)
print gc.is_tracked(w)
print gc.get_referrers(f)
print gc.get_referrers(w)
print gc.get_referrers(f)[0]['f']

del f, w
print gc.collectable()
print gc.is_tracked(f)
print gc.is_tracked(w)
print gc.get_referrers(f)
print gc.get_referrers(w)
print gc.get_referrers(f)[0]['f']

print gc.collect()

print gc.collectable()
print gc.is_tracked(f)
print gc.is_tracked(w)
print gc.get_referrers(f)
print gc.get_referrers(w)
print gc.
