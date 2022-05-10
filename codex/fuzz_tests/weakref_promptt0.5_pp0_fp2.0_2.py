import weakref
# Test weakref.ref() with a mutable object.

# Create an object to be referenced
class Foo:
    pass

foo = Foo()
foo.x = 1

# Create a weakref to the object
foo_ref = weakref.ref(foo)

# Check that the weakref works
assert foo_ref() is foo
assert foo_ref().x == 1

# Delete the object
del foo

# Check that the weakref is dead
assert foo_ref() is None
