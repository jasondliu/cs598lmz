import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without starting a new collection
gc.collect()

print "all objects:", gc.get_objects()
print "collectable objects:", gc.get_objects(gc.COLLECTABLE)
# Test gc.collect() with starting a new collection
gc.collect(2)

print "all objects:", gc.get_objects()
print "collectable objects:", gc.get_objects(gc.COLLECTABLE)
gc.set_debug(0)

print "all objects:", gc.get_objects()
print "collectable objects:", gc.get_objects(gc.COLLECTABLE)
gc.collect()

print "all objects:", gc.get_objects()
print "collectable objects:", gc.get_objects(gc.COLLECTABLE)
gc.collect()

print "all objects:", gc.get_objects()
print "collectable objects:", gc.get_objects(gc.COLLECTABLE)
gc.collect()

print "all objects:", gc.get_objects()
print "collectable
