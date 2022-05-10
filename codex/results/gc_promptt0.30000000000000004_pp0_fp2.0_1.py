import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class C:
    pass

# Create a reference cycle
c = C()
d = C()
c.x = d
d.x = c

# Create a weakref to the cycle
w = weakref.ref(c)

# Enter the reference cycle in a function
def f():
    l = [c, d]

# Create a reference to the function, keeping it alive
r = f

# Trigger a full collection
gc.collect()

# Check that the weakref is still alive
print w() is c

# Check that the function is still alive
print r() is None

# Check that the objects are still alive
print c.x is d
print d.x is c

# Check that the weakref is still alive
print w() is c

# Check that the function is still alive
print r() is None

# Check that the objects are still alive
print c.x is d
print d.x is c

# Check that the weakref is still alive
print w() is c

# Check that the function is still alive
