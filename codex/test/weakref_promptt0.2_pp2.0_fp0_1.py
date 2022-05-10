import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()

# Create a weak reference to f
r = weakref.ref(f)

# Print the object referred to by the weak reference
