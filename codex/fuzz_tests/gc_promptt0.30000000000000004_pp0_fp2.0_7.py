import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    c = C()
    wr = weakref.ref(c)
    del c
    return wr

# Create a reference cycle
wr = f()

# Collect the cycle
gc.collect()

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr() is None

# Check that the object was collected
assert wr()
