import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()

# Create a reference cycle
a.b = a

# Create a reference to the object
w = weakref.ref(a)

print('Before:', w())

# Remove the only remaining reference to the object (a)
del a

# Trigger a collection.
gc.collect()

print('After:', w())

# Test gc.get_objects()

import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class A:
    pass

a = A()

# Create a reference cycle
a.b = a

# Create a reference to the object
w = weakref.ref(a)

print('Before:', w())

# Remove the only remaining reference to the object (a)
del a

# Trigger a collection.
gc.collect()

print('After:', w())

# Test gc.get_referrers()

import gc

class A:
    pass

a = A()

# Create
