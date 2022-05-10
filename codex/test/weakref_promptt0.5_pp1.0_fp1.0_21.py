import weakref
# Test weakref.ref() with a callable object.
import weakref

# Create a reference to a callable object.
def f():
    pass
r = weakref.ref(f)

# Test the reference.
assert r() is f

# Delete the original object, and test the reference.
del f
assert r() is None
# Test weakref.ref() with a callable object.
import weakref

# Create a reference to a callable object.
def f():
    pass
r = weakref.ref(f)

# Test the reference.
assert r() is f

# Delete the original object, and test the reference.
del f
assert r() is None
# Test weakref.ref() with a callable object.
import weakref

# Create a reference to a callable object.
def f():
    pass
r = weakref.ref(f)

# Test the reference.
assert r() is f

# Delete the original object, and test the reference.
del f
assert r() is None
# Test weakref.ref() with a callable object.
