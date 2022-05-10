import weakref
# Test weakref.ref(object)

class Foo:
    pass

foo = Foo()

# Create a weak reference to foo
foo_ref = weakref.ref(foo)

# Get the object back
foo_object = foo_ref()

# Print the object
print(foo_object)

# Delete the object
del foo

# Print the object
print(foo_object)

# Get the object back
foo_object = foo_ref()

# Print the object
print(foo_object)

# Test weakref.proxy(object)

class Foo:
    pass

foo = Foo()

# Create a weak reference to foo
foo_ref = weakref.proxy(foo)

# Get the object back
foo_object = foo_ref()

# Print the object
print(foo_object)

# Delete the object
del foo

# Print the object
print(foo_object)

# Get the object back
foo_object = foo_ref()

# Print the object
print(foo_object)

