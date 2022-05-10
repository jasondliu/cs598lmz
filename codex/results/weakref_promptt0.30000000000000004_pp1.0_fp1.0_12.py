import weakref
# Test weakref.ref(x)
#
# Note: This test is not really a test of weakref.ref().  It is a test
# of the weakref module's ability to create weak references to
# objects.  The weakref.ref() function is just a convenience function
# that creates a weak reference and returns it.

# Create a weak reference to an object
x = weakref.ref(42)

# Check that the weak reference can be called
print(x())

# Check that the weak reference can be used as a boolean
if x:
    print("x is not None")

# Check that the weak reference can be used as a boolean
if not x:
    print("x is None")

# Check that the weak reference can be used in a comparison
if x == 42:
    print("x is 42")

# Check that the weak reference can be used in a comparison
if x != 42:
    print("x is not 42")

# Check that the weak reference can be used in a comparison
if x is 42:
    print("x is 42")

# Check that the weak reference can be used
