import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
w = weakref.ref(gc.collect())
if type(w()) != int:
    raise Exception, "gc.collect() did not return an integer"

# Test gc.get_objects()
if len(gc.get_objects()) != 2:
    raise Exception, "wrong number of objects tracked by gc"

# Test gc.get_count()
if len(gc.get_count()) != 2:
    raise Exception, "wrong number of items in gc.get_count() return val"

# Test gc.get_threshold()
if len(gc.get_threshold()) != 3:
    raise Exception, "wrong number of items in gc.get_threshold() return val"

# Test gc.set_threshold()
gc.set_threshold(100, 10, 10)
if gc.get_threshold() != (100, 10, 10):
    raise Exception, "gc.get_threshold() != gc.set_threshold(100, 10, 10)"

gc.set_threshold(1, 2,
