import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The garbage collector collects all unreachable objects.
# The unreachable objects are those that are unreachable from any
# reference in the local namespace.  This includes objects that are
# reachable from the local namespace, but are not reachable from
# global namespaces.

class C:
    pass

# Create a cycle
c = C()
c.x = c

# Create a reference to the cycle
d = c.x

# Remove all references to the cycle
c = None
d = None

# Collect the cycle
gc.collect()

# Verify that the cycle is gone
print(gc.collect())

# Create a cycle
c = C()
c.x = c

# Create a reference to the cycle
d = c.x

# Remove all references to the cycle
c = None
d = None

# Verify that the cycle is not collected
print(gc.collect())

# Create a cycle
c = C()
c.x = c

# Create a reference to the cycle
d = c.x

# Remove all references to the cycle

