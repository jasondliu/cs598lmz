import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect:
gc.collect()
print(gc.collect())
gc.collect()
print(gc.collect())
print(gc.garbage)

# Test bug-fix in is_tracked:
gc.is_tracked(object())
print(gc.is_tracked({}))

# Exercise issue 1726034.  is_tracked should not be true of *weakref* objects
# that are in gc.garbage.
class Bar(object):
    pass

def decr_ref(r):
    r().attr = None

def test_ref(foo):
    # decr_ref retains a reference to r, so gc never observes that foo is
    # no longer strongly referenced.  It therefore remains tracked and is
    # eventually finalized when it winds up in gc.garbage.
    weak_foo = weakref.ref(foo, decr_ref)
    gc.collect()
    print(gc.collect())
    print(gc.is_tracked(foo))
    print(dict(gc.get_objects()))
    print(gc.
