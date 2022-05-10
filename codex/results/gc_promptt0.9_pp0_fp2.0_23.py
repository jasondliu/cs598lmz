import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a finalizer on an object.

# The most reliable test is to use a weakref callable, which will
# be called once (if ever) during collection, and only once:
weaker = False  # weakref callback was called?
weak_called = weak_called2 = None

def finalize():
    global weaker, weak_called, weak_called2
    weaker = True
    weak_called = weak_called2

l = []
obj = type('obj', (object,), {})()
weak_called = weakref.ref(obj, finalize)   # weak callable
weak_called2 = weakref.ref(obj)            # weak back-pointer

# Make sure garbage collection is enabled.
gc.enable()

# Run the collection pass.
# XXX: If this doesn't collect obj, this test is useless.
assert gc.collect() == 1, gc.collect()

assert weaker, weak_called2
assert not weak_called()
assert not weak_called2()

# Check that calling gc.collect again doesn't call the finalizer again.
