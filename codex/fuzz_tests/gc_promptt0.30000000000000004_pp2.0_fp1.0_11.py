import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

class C:
    pass

# Create a reference cycle
c = C()
d = C()
c.foo = d
d.foo = c

# Create a weakref to one of the objects
w = weakref.ref(c)

# Collect
n = gc.collect()
print(n)

# Check that the weakref is dead
print(w())

# Check that the cycle was collected
print(gc.garbage)

# Create a weakref to the other object
w = weakref.ref(d)

# Collect
n = gc.collect()
print(n)

# Check that the weakref is dead
print(w())

# Check that the cycle was collected
print(gc.garbage)

# Create a weakref to the cycle
w = weakref.ref(c)

# Collect
n = gc.collect()
print(n)

# Check that the weakref is dead
print(w())

# Check that the cycle was collected
print(gc.garbage)


