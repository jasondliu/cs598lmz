import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

def f():
    return 42

# Check that collectable objects are collected
w = weakref.ref(f)
gc.collect()
assert w() is None

# Check that collectable objects are collected
w = weakref.ref(f)
del f
gc.collect()
assert w() is None


# Check that collectable objects are not collected
w = weakref.ref(f)
del f
gc.collect()
assert w() is not None

# Check that collectable objects are collected
w = weakref.ref(f)
gc.collect()
assert w() is None

# Check that collectable objects are collected
w = weakref.ref(f)
del f
gc.collect()
assert w() is None

# Check that collectable objects are collected
w = weakref.ref(f)
del f
gc.collect()
assert w() is None

# Check that collectable objects are collected
w = weakref.ref(f)
del f
gc.collect()
assert w() is None

gc.set_
