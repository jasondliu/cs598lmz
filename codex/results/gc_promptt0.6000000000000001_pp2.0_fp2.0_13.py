import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without VERBOSE flag
gc.collect()

# Test gc.collect() with VERBOSE flag
gc.collect(1)

# Test gc.collect() with VERBOSE and DEBUG_COLLECTABLE flags
gc.collect(2)

# Test gc.collect() with VERBOSE, DEBUG_COLLECTABLE and DEBUG_UNCOLLECTABLE flags
gc.collect(3)

# Test gc.collect() with VERBOSE, DEBUG_COLLECTABLE, DEBUG_UNCOLLECTABLE and DEBUG_INSTANCES flags
gc.collect(4)

# Test gc.collect() with VERBOSE, DEBUG_COLLECTABLE, DEBUG_UNCOLLECTABLE, DEBUG_INSTANCES and DEBUG_OBJECTS flags
gc.collect(5)

# Test gc.collect() with VERBOSE, DEBUG_COLLECTABLE, DEBUG_UNCOLLECTABLE, DEBUG_INSTANCES, DEBUG_OBJECTS and DEBUG_SAVEALL flags
gc.collect(6)

# Test gc.collect() with VERBOSE, DEBUG_COLLECTABLE, DEBUG_
