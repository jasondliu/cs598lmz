import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method that prints a message when
# the instance is destroyed.

class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "deleting", self.name

# Create an instance of C and get a weak reference to it.

c = C("first")
r = weakref.ref(c)
print "created", c.name

# Create a weakly-referenced instance of C, and get a weak reference to it.

c2 = C("second")
r2 = weakref.ref(c2)
print "created", c2.name

# Create a weakly-referenced proxy for c2.

p = weakref.proxy(c2)

# Test the weak references.

print "via instance:", r().name
print "via instance:", r2().name
print "via proxy:", p.name

# Delete the instances.

del c, c2

# Verify
