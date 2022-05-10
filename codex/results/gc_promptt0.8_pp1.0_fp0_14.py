import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
o = C()
assert weakref.getweakrefcount(o) == 0
assert gc.get_referents(o) == []
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1
assert gc.get_referents(o) == [r]
assert r() is o
o2 = C()
assert gc.collect() == 1
assert r() is None
assert weakref.getweakrefcount(o) == 0
assert gc.get_referents(o) == []
# Test gc.garbage.
o = C()
r = weakref.ref(o)
assert r() is o
assert weakref.getweakrefcount(o) == 1
del o, r
gc.collect()
assert gc.garbage == []

# test that gc.garbage isn't cleared by direct calls to gc.collect
class V(object):
    pass
o = V()
o.o = o
gc.garbage.append(o)
assert len(gc.garbage)
