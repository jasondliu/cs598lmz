import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.collect()
wr = weakref.ref(gc.collect())
assert wr() is None
gc.collect()
assert wr() is None

# Test gc.collect(2)
wr = weakref.ref(gc.collect(2))
assert wr() is None
gc.collect(2)
assert wr() is None

# Test gc.collect(1)
wr = weakref.ref(gc.collect(1))
assert wr() is None
gc.collect(1)
assert wr() is None

# Test gc.collect(0)
wr = weakref.ref(gc.collect(0))
assert wr() is None
gc.collect(0)
assert wr() is None

# Test gc.collect(-1)
wr = weakref.ref(gc.collect(-1))
assert wr() is None
gc.collect(-1)
assert wr() is None

# Test gc.collect(-2)
wr = weakref.ref(gc.collect(-2))
assert wr() is None
gc.collect(-2)
assert wr() is None
