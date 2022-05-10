import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
objects = [{}, {}, {}, {}]
for o in objects:
    r = weakref.ref(o)
    print r(), gc.is_tracked(o)
    assert gc.is_tracked(o)
del o  # Remove last reference to the object
gc.collect()
for o in objects:
    print o, gc.is_tracked(o)
    assert not gc.is_tracked(o)

# Test gc.get_referents()
# Note: there is no *efficient* and *explicit* way to know the referents,
# because the only available API is a call to collect() returning a list of
# objects that survived. We have to re-implement the full GC logic here to
# simulate the collect pass based on reachability.
# Bug: wrongly returns unreachable instances that are referred in the stack


def gc_get_referents(roots):
    """Simulates a collect pass, returns all reachable objects from roots."""
    gc.collect()
    # find all reachable objects
