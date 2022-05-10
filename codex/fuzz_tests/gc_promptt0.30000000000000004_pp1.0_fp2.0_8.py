import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a cycle
class A:
    pass
a = A()
a.b = A()
a.b.a = a

# Create a weak reference to the cycle
wr = weakref.ref(a)
print wr() is a

# Break the cycle
a = None

# Collect the cycle
gc.collect()

# The weak reference should now be dead
print wr() is None

# Create a cycle
class A:
    pass
a = A()
a.b = A()
a.b.a = a

# Create a weak reference to the cycle
wr = weakref.ref(a)
print wr() is a

# Break the cycle
a = None

# Collect the cycle
gc.collect()

# The weak reference should now be dead
print wr() is None

# Create a cycle
class A:
    pass
a = A()
a.b = A()
a.b.a = a

# Create a weak reference to the cycle
wr = weakref.ref(a)
print wr() is a

#
