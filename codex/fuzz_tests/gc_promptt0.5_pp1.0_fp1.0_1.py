import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Create a weakref
a = weakref.ref(object())
# Create a cycle
b = object()
b.attr = b
# Create a weakref to the cycle
c = weakref.ref(b)
# Collect uncollectable objects
gc.collect()
# Print the weakrefs
print(a, c)
# Print the objects
print(a(), c())

# Create a weakref to the cycle
c = weakref.ref(b)
# Collect uncollectable objects
gc.collect()
# Print the weakrefs
print(a, c)
# Print the objects
print(a(), c())
