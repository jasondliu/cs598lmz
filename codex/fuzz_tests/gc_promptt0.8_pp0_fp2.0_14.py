import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Test:
  pass

# Test that collectable() returns 1 at the right times
gc.collect()
t = Test()
assert gc.collectable(t) == 1
assert gc.collect() == 0
assert gc.collectable(t) == 0

# Test that collect() does not collect if collectable() is 0
t1 = Test()
weakref_t = weakref.ref(t1)
t1 = None
assert weakref_t() is None
gc.collect()
assert gc.collectable(weakref_t) == 0
assert gc.collectable(weakref_t()) == 0
assert gc.collect() == 0
assert gc.collectable(weakref_t) == 0
assert gc.collectable(weakref_t()) == 0

# Test that calling a function that contains collectable() in the locals of
# the frame that calls it has no side effects
gc.disable()
def call_collectable(i):
  x = Test()
  y = Test()
  if i == 0:
    return g
