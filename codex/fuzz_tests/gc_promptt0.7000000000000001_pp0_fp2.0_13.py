import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
wr = weakref.ref(gc.collect())
assert wr() is not None
gc.collect()
assert wr() is None

# Test gc.garbage
objs = [gc.collect() for i in range(100)]
collectable = gc.garbage
assert len(collectable) == len(objs)

# Test gc.disable()
gc.disable()
gc.collect()
assert len(gc.garbage) == len(collectable)

# Test gc.enable()
gc.enable()
gc.collect()
assert len(collectable) > len(gc.garbage)

# Test gc.isenabled()
assert gc.isenabled()
gc.disable()
assert not gc.isenabled()
gc.enable()
assert gc.isenabled()

# Test gc.get_threshold()
old_threshold = gc.get_threshold()
gc.set_threshold(1000, 10, 10)
new_threshold = gc.get_threshold()
assert old_threshold != new_th
