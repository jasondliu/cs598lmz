import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Initialize C level variables
gc.collect()
class Foo:
    pass

# Create a few objects
f = Foo()
g = Foo()
h = Foo()
f.x = Foo()
f.x.y = f
g.x = f.x
h.x = f.x
f.x.y = h
count = gc.collect()
#print count
assert count == 3

# Test gc.get_threshold()
count = gc.get_threshold()
assert len(count) == 3

# Test gc.set_threshold()
gc.set_threshold(18, 12, 12)
count = gc.get_threshold()
assert count == (18, 12, 12)
gc.set_threshold(1, 2, 3)

# Test gc.get_objects()
objs = gc.get_objects()
assert isinstance(objs, list)
assert len(objs) > 0
#print len(objs)

# Test gc.get_stats()
stats = g
