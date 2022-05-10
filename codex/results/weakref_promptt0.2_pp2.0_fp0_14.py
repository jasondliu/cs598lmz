import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a method
class Foo:
    def __init__(self, name):
        self.name = name
    def method(self):
        print self.name

# Create an instance of Foo
f = Foo('fred')

# Create a weak reference to f
r = weakref.ref(f)

# Create a weak proxy to f
p = weakref.proxy(f)

# Check that the proxy and reference work
print r().name
print p.name

# Delete the original object
del f

# Check that the proxy and reference still work
print r().name
print p.name

# Check that the proxy and reference still work
print r().method()
print p.method()

# Check that the proxy and reference still work
print r().method
print p.method

# Check that the proxy and reference still work
print r().method.__self__
print p.method.__self__

# Check that the proxy and reference still work
print r().method.__self__()
print p.method.
