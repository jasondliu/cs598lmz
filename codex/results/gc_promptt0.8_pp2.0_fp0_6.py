import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
gc.collect(1)
gc.collect(1, 1)

# Test gc.get_debug
assert gc.get_debug() == gc.DEBUG_COLLECTABLE

# Test gc.is_tracked
assert gc.is_tracked('abcd') == 0
assert gc.is_tracked(3.14) == 0
assert gc.is_tracked(1000) == 1
assert gc.is_tracked(1.0) == 1
assert gc.is_tracked(xrange(1000)) == 1
assert gc.is_tracked(bytearray('abcd')) == 1
assert gc.is_tracked(weakref.ref('abcd')) == 1
assert gc.is_tracked(tuple(xrange(1000))) == 1

# Test gc.disable, gc.isenabled
assert gc.isenabled() == 1
gc.disable()
assert gc.disable() == 0
assert gc.isenabled() == 0
gc.enable()
assert
