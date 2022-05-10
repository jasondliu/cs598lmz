import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    pass
gc.collect()
del f
gc.collect()

# Test is_tracked() with a weakref
def f():
    pass
assert gc.is_tracked(f)
r = weakref.ref(f)
gc.collect()
assert gc.is_tracked(f)
assert gc.is_tracked(r)
del r, f
gc.collect()
assert not gc.is_tracked(r)
assert not gc.is_tracked(f)

# Test get_referrers()
def f():
    pass
assert gc.get_referrers(f) == []
r = weakref.ref(f)
assert gc.get_referrers(f) == [{'f': f, 'r': r}]
del r, f
gc.collect()
assert gc.get_referrers(f) == []

# Test get_referents()
def f():
    pass
assert gc.get_referents(f) == [f
