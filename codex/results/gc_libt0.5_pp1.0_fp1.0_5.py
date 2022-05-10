import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

# Create a reference cycle
a = MyClass('a')
b = MyClass('b')
a.b = b
b.a = a

# Create a weak reference to a
c = weakref.ref(a)
print c

# Remove all references to a and b
a = None
b = None

print c

# Delete any remaining references
gc.collect()

print c
