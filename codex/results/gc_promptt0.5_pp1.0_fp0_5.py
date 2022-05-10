import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
r = weakref.ref(gc.collect())
gc.collect()
print gc.is_tracked(r())
gc.collect()
print gc.is_tracked(r())

# Test gc.collect(2)
r = weakref.ref(gc.collect(2))
gc.collect(2)
print gc.is_tracked(r())
gc.collect(2)
print gc.is_tracked(r())

# Test gc.garbage
r = weakref.ref(gc.garbage)
gc.collect(2)
print gc.is_tracked(r())
gc.collect(2)
print gc.is_tracked(r())

# Test gc.get_count()
r = weakref.ref(gc.get_count())
gc.collect(2)
print gc.is_tracked(r())
gc.collect(2)
print gc.is_tracked(r())

# Test gc.get_debug()
r = weakref.ref(gc.get
