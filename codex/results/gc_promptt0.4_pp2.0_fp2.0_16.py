import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.collect(1).
# This is a pretty weak test.  It just makes sure the calls don't crash.
gc.collect()
gc.collect(1)
gc.collect(2)
gc.collect(1)
gc.collect(0)
gc.collect(2)
gc.collect(0)
gc.collect(1)
gc.collect()
# Test gc.garbage.
# XXX This test is pretty weak too.
gc.garbage
# Test gc.get_count().
gc.get_count()
gc.get_count()
gc.get_count()
# Test gc.get_debug() and gc.set_debug().
gc.get_debug()
gc.set_debug(0)
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc
