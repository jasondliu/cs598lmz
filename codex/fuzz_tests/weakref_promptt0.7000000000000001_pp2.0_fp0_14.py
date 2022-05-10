import weakref
# Test weakref.ref()
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

a = Foo('a')              # Create a reference
wr = weakref.ref(a)       # Create a weak reference
print wr()                # Evaluate the weak reference
del a                     # Delete the reference
print wr()                # The value of the weak reference is None

# Test weakref.proxy()
import weakref

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

a = Foo('a')              # Create a reference
wp = weakref.proxy(a)     # Create a proxy
print wp.name             # Access some attribute
del a                     # Delete the reference
print wp.name             # Access some attribute

# Test weakref.WeakValueDictionary
import weakref

class Foo
