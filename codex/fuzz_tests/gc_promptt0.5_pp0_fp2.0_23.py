import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A(object):
    pass

class B(object):
    pass

# Create a reference cycle
a = A()
b = B()
a.b = b
b.a = a


# Create some objects
for i in range(10):
    A()
    B()

# Break the reference cycle
a = None
b = None

# Collect
gc.collect()

# Get the list of collectable objects
objects = gc.get_objects()

# Print the number of collectable objects
print('Collectable objects:', len(objects))

# Print the first 10 objects
for o in objects[:10]:
    print(o)

# Print the types of the first 10 objects
for o in objects[:10]:
    print(type(o))

# Print the types of the first 10 collectable objects
for o in objects[:10]:
    if isinstance(o, (A, B)):
        print(type(o))

# Print the number of A and B instances
print('A instances:', sum(isinstance
