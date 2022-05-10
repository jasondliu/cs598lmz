import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without any arguments
gc.collect()
# Test gc.collect() with a single argument
gc.collect(1)
# Test gc.collect() with a list argument
gc.collect([1, 2, 3])
# Test gc.collect() with a tuple argument
gc.collect((1, 2, 3))
# Test gc.collect() with a dict argument
gc.collect({'a': 1, 'b': 2})
# Test gc.collect() with a set argument
gc.collect(set([1, 2, 3]))
# Test gc.collect() with a frozenset argument
gc.collect(frozenset([1, 2, 3]))
# Test gc.collect() with a string argument
gc.collect('abc')
# Test gc.collect() with a weakref argument
gc.collect(weakref.ref(42))
# Test gc.collect() with an integer argument
gc.collect(42)
# Test gc.collect() with an object argument
gc.collect(object())
# Test gc.collect() with a slice argument
gc.
