import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
# Test garbage collecting a weakrefable instance
x = C()
w = weakref.ref(x)
assert w() is x
gc.collect()
assert w() is None
assert len(gc.garbage) == 0

# Test garbage collecting a weakrefable instance with __del__
# that resurrects itself
x = D()
w = weakref.ref(x)
assert w() is x
gc.collect()
assert w() is None
assert len(gc.garbage) == 0

# Test garbage collecting a weakrefable instance with __del__
# that resurrects something else

x = E()
w = weakref.ref(x)
assert w() is x
gc.collect()
assert w() is None
assert len(gc.garbage) == 0
