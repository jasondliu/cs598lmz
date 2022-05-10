import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with debug output off
op_cnt = gc.collect()
gc.set_debug(gc.DEBUG_STATS)
# All collectable objects should be in the root set but may not be
# present on a generational system that collects only the nursery
# on each collection.
ref = weakref.ref(A())
a = A()
b = [a]
del a, b
gc.collect()
c = C()
c.x = B()
d = [c]
del c, d
gc.collect()
e = E(123)
e2 = [e]
del e
gc.collect()
f = F([])
f2 = [f]
del f, f2
gc.collect()
if D and type(create_testconn()) is D:
    g = D()
    g2 = [g]
    del g, g2
    gc.collect()
gc.set_debug(gc.DEBUG_LEAK)
# Call callbacks again in case some objects were finalized
op_cnt = gc.collect()
print('finalized objects')
