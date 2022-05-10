import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()

# Create a reference cycle
a.x = b
b.x = a

# Create a reference to the cycle
c = weakref.ref(a)

# Break the cycle
a = None
b = None

# Collect the cycle
gc.collect()

# The cycle is gone
print(c())

# Test gc.get_referrers()

class A:
    pass

a = A()
b = A()

# Create a reference cycle
a.x = b
b.x = a

# Create a reference to the cycle
c = weakref.ref(a)

# Break the cycle
a = None
b = None

# Collect the cycle
gc.collect()

# The cycle is gone
print(c())

# Test gc.get_referrers()

class A:
    pass

a = A()
b = A()

# Create a reference cycle
a.x = b
b.x = a


