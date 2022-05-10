import weakref
# Test weakref.ref(x)

# Create a weak reference to an object
class Foo:
    pass

x = Foo()
r = weakref.ref(x)

# Test the weak reference
assert r() is x
assert r() is not None

# Delete the object
del x

# Test the weak reference
assert r() is None
# Test weakref.ref(x, callback)

# Create a weak reference to an object
class Foo:
    pass

x = Foo()

# Create a list to store the callback calls
calls = []

# Create a weak reference to the object
r = weakref.ref(x, lambda w: calls.append(w))

# Test the weak reference
assert r() is x
assert r() is not None

# Delete the object
del x

# Test the weak reference
assert r() is None

# Test the callback
assert len(calls) == 1
assert calls[0]() is None
# Test weakref.getweakrefcount(x)

# Create a weak reference to an object
class Foo:
    pass

