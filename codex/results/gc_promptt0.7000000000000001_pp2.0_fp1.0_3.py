import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def create_cycle():
    l = [{}]
    l[0]['l'] = l
    return weakref.ref(l)

print len(gc.get_objects())
for i in range(100):
    r = create_cycle()
    print len(gc.get_objects())

print len(gc.get_objects())
gc.collect()
print len(gc.get_objects())

# Test gc.garbage
# Make a cyclic trashcan
# for collectable objects
l = []
d = {}
l.append(d)
d['l'] = l

# Register it
gc.garbage.append(l)

# Save the old thresholds
old_thresholds = gc.get_threshold()

# Set thresholds low
gc.set_threshold(1)

# Verify the trashcan is not collected
print gc.collect()

# Verify the trashcan is collected
# by lowering the thresholds
gc.set_threshold(0)
gc.collect()

# Restore thresholds
gc.set_
