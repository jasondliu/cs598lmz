import weakref
# Test weakref.ref() for objects that implement __del__.

# Create a class with a __del__ method.
class C:
    def __init__(self):
        self.x = 1
    def __del__(self):
        self.x = None

# Create an instance.
c = C()

# Test weakref.ref() with the instance.
r = weakref.ref(c)
# Check that r() returns the instance.
if r() is not c:
    raise TestFailed("r() should return c")
# Check that the instance is still alive.  (This will fail if the test
# fails, but we won't be able to see the failure.)
if c.x is None:
    raise TestFailed("c shouldn't be dead yet")
# Delete the instance.
del c
# Check that r() returns None.
if r() is not None:
    raise TestFailed("r() should return None")

# Create an instance.
c = C()

# Test weakref.ref() with a callable object that uses an instance's
# __del__ method
