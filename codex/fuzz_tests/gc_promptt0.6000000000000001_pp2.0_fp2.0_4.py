import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class A:
    pass

def check_refs(remaining):
    collected = [obj for obj in gc.garbage if isinstance(obj, A)]
    gc.garbage[:] = [obj for obj in gc.garbage if not isinstance(obj, A)]
    assert len(collected) == len(remaining), "collected %s, remaining %s" % (
        len(collected), len(remaining))
    for obj in collected:
        assert obj() is None, "cyclic reference"
    for obj in remaining:
        assert obj() is not None, "reference missing"

w = weakref.ref(A())

gc.collect()
check_refs([w])

w = weakref.ref(A())
w2 = weakref.ref(A())

gc.collect()
check_refs([w, w2])

w = weakref.ref(A())
w2 = weakref.ref(A())
del w2

gc.collect()
check_refs
