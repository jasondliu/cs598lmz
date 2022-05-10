import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

# Test gc.get_stats()
gc.get_stats()

# Test gc.set_debug()
for i in range(3):
    gc.set_debug(gc.DEBUG_STATS)
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    gc.set_debug(gc.DEBUG_COLLECTABLE)
    gc.set_debug(gc.DEBUG_INSTANCES)
    gc.set_debug(gc.DEBUG_OBJECTS)
    gc.set_debug(gc.DEBUG_SAVEALL)
    gc.set_debug(gc.DEBUG_LEAK)

# Test gc.get_debug() and debug flags
print gc.get_debug()
gc.set_debug(gc.DEBUG_STATS)
print gc.get_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print gc.get_debug()
gc.set_debug(
