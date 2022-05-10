import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name

# Create some instances
c1 = C("c1")
c2 = C("c2")
c3 = C("c3")

# Create weak references to them
r1 = weakref.ref(c1)
r2 = weakref.ref(c2)
r3 = weakref.ref(c3)

# Create weak proxies to them
p1 = weakref.proxy(c1)
p2 = weakref.proxy(c2)
p3 = weakref.proxy(c3)

# Check that they work
print r1().name
print r2().name
print r3().name
print p1.name
print p2.name
print p3.name

# Delete references to c1 and c2
del c1, c2

# Check that they are gone
print r1()

