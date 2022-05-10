import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
# The remaining tests in this file are not worth running if gc.collect()
# doesn't find the uncollectable object.
def f():
    x = []
    x.append(x)
    return x

x = f()
del f

# Find everything that's reachable from the global dict
wr = weakref.ref(globals())
gc.collect()

print(gc.garbage)

# There should be only one object in gc.garbage:  the list created by f()
assert len(gc.garbage) == 1 and gc.garbage[0] is x, gc.garbage

# There should be no weakrefs to gc.garbage[0]
assert len(gc.get_referents(gc.garbage[0])) == 1, gc.get_referents(gc.garbage[0])
assert gc.get_referrers(gc.garbage[0]) == [gc.garbage], gc.get_referrers(gc.garbage[0])
