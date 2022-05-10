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
