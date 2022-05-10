import weakref
# Test weakref.ref() and weakref.proxy()

# Create a new class
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(' + self.name + ')'

# Create an instance
f = Foo('bar')

# Create a weak reference
r = weakref.ref(f)

# Create a weak-proxy
p = weakref.proxy(f)

# Check that the objects work
print f, p, r
print f.name, p.name, r().name

# Delete the original object
del f

# Check that the weak references still exist
print p, r

# Check that the weak references now raise an exception
try:
    print p.name, r().name
except ReferenceError:
    print 'ReferenceError'

# Check that weak-proxy objects are usable as dictionary keys
d = {p: 1}
print d[r()]

# Create a new instance
f = Foo('baz')

# Check that the weak references now refer to
