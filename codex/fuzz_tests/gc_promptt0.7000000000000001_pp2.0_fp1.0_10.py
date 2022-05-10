import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The following is a simple test of gc.collect().  It is based on the
# example in the Python Library Reference Manual:

gc.collect()
assert gc.collect() == 0
l = [1, 2, 3]
l = [l, l]
assert gc.collect() == 0
del l
assert gc.collect() == 5

# Test gc.get_objects()
#
# The following is a simple test of gc.get_objects().  It is based on the
# example in the Python Library Reference Manual:

gc.collect()
assert len(gc.get_objects()) == 0
l = [1, 2, 3, 4, 5]
assert len(gc.get_objects()) == 1
l2 = l[:]
assert len(gc.get_objects()) == 2
del l, l2
assert len(gc.get_objects()) == 0

# Test gc.get_referrers()
#
# The following is a simple test of gc.get_referrers().  It is based on the
# example
