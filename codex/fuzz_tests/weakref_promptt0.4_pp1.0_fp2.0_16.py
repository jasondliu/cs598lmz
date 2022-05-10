import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __del__(self):
        print("del")

# Create an instance of the class
c = C()

# Create a weak reference to the instance
r = weakref.ref(c)

# Create a weak reference to the instance through a proxy
p = weakref.proxy(c)

# Check that the proxy references the same object
assert(p is c)

# Check that the weak reference and proxy reference the same object
assert(r() is p)

# Delete the original reference to the object
del c

# Check that the object still exists through the proxy
assert(p is not None)

# Check that the object still exists through the weak reference
assert(r() is not None)

# Delete the proxy
del p

# Check that the object still exists through the weak reference
assert(r() is not None)

# Delete the weak reference
del r

# Check that the object has been deleted
try:
    p
except NameError:
    print
