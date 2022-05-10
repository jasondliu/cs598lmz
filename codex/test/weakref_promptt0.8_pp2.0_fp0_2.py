import weakref
# Test weakref.ref constructor with old-style class instance

class A:
    pass

# Make instances
instances = [A() for i in range(3)]

for instance in instances:
    # Make a weak reference for each instance
    wr = weakref.ref(instance)
    # Resolve the weak reference
    instance = wr()
    # Check
    print(instance, wr())
