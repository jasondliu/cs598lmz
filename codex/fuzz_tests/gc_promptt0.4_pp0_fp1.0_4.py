import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
a.b = A()

# Create a reference cycle
a.b.a = a

# Create a reference to the object
a_ref = weakref.ref(a)

# Remove all references to the object
del a
del a_ref

# Collect the object
gc.collect()

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

# Print the number of objects collected and uncollectable
print(gc.collect())
print(gc.garbage)

