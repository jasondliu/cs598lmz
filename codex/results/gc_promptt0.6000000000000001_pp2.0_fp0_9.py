import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.DEBUG_COLLECTABLE.

class A:
    pass

# Create a chain of objects, A -> A -> ...
# Use a weakref so the chain is broken when the last A is gone.
c = weakref.ref(A())
for i in range(100):
    c = A()
    c.next = weakref.ref(c)

# Collect the chain.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that the chain is broken.
gc.collect()

# Verify that
