import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after gc.DEBUG_COLLECTABLE is set
gc.collect()
# Test weakref with a weakly reachable object
r = weakref.ref(C())
gc.collect()
# Test weakref with an unreachable object
r = weakref.ref(C())
del r
gc.collect()
# Test weakref with a reachable object
r = weakref.ref(C())
gc.collect()
# Test cyclic gc with a self-referential object
r = C()
r.x = r
gc.collect()
# Test cyclic gc with two self-referential objects
r = C()
s = C()
r.x = s
s.x = r
gc.collect()
# Test cyclic gc with three self-referential objects
r = C()
s = C()
t = C()
r.x = s
s.x = t
t.x = r
gc.collect()
# Test cyclic gc with a reachable, self-referential object
r = C()
r.x = r
gc.collect()
#
