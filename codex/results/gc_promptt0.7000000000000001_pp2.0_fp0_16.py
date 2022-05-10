import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
# Create a cycle and make sure it gets collected.
# Also check that we can break the cyclic dependency in a callback.

l = []

class A:
    def __del__(self):
        l.append(None)
        print "removing A", self
        self.__dict__.clear()

class B:
    def __del__(self):
        l.append(None)
        print "removing B", self
        self.__dict__.clear()

a = A()
b = B()

a.b = b
b.a = a

print "Checking for cyclic references..."
gc.collect()
print "Allocating a lot of data..."
# force a collection
l = []
for i in xrange(100000):
    l.append(str(i))
print "Collecting again..."
gc.collect()
print "Done."
