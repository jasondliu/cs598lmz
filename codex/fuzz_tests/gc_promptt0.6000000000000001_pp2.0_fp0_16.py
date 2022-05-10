import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a callback
gc.collect()
# Test gc.collect() with a callback
def callback(ignored):
    print('called back')

gc.collect(callback)
# Test gc.collect() with a callback that raises an exception
def boom(ignored):
    raise RuntimeError

gc.collect(boom)
# Test gc.collect() with a callback that returns an integer
def return_42(ignored):
    return 42

gc.collect(return_42)
# Test gc.collect() with a callback that returns a float
def return_42_point_0(ignored):
    return 42.0

gc.collect(return_42_point_0)
# Test gc.collect() with a callback that returns a string
def return_42_point_0(ignored):
    return '42.0'

gc.collect(return_42_point_0)
# Test gc.collect() with a callback that returns a tuple
def return_42_point_0(ignored):
    return ('foo', 'bar')

gc.
