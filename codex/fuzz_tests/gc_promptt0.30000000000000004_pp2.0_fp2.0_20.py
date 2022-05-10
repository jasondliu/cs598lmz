import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with no uncollectable objects.
gc.collect()
# Test gc.collect() with one uncollectable object.
gc.collect()
# Test gc.collect() with two uncollectable objects.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object with a __del__ method.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object with a __del__ method
# that raises an exception.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object with a __del__ method
# that raises an exception that is caught.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object with a __del__ method
# that raises an exception that is caught and raises another exception.
gc.collect()
# Test gc.collect() with a cyclic uncollectable object with a __del__ method
# that raises an exception that is caught and raises another exception that is
# caught
