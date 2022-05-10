import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

print()

# Create a list of garbage
for i in range(10):
    x = [i]

# Print garbage
gc.collect()

print()

# Create a list of garbage
for i in range(10):
    x = {i: i}

# Print garbage
gc.collect()

print()

# Create a list of garbage
for i in range(10):
    x = weakref.ref(i)

# Print garbage
gc.collect()
