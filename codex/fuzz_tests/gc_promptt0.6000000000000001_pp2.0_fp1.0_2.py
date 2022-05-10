import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in various states
for i in range(4):
    gc.collect()
    # Create a cycle and make it unreachable
    l = []
    l.append(l)
    wr = weakref.ref(l)
    del l
    gc.collect()
    # Create a new cycle and make it unreachable
    l = []
    l.append(l)
    wr = weakref.ref(l)
    del l
    gc.collect()
    # Break the cycle, and check if the object can be collected
    l = wr()
    l.pop()
    del l
    gc.collect()
    # Create a cycle, and check if the object can be collected
    l = []
    l.append(l)
    wr = weakref.ref(l)
    del l
    gc.collect()
    # Break the cycle, and check if the object can be collected
    l = wr()
    l.pop()
    del l
    gc.collect()
# Check if gc.garbage contains only non-collectable objects

