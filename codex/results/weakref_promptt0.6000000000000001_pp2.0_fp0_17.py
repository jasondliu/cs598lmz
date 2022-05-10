import weakref
# Test weakref.ref

# The weakref module provides a proxy object that weakly references an object.
# The following example creates a weak reference to an object, and then
# prints the weak reference, the referenced object, and the string
# representation of the referenced object.

class Foo:
    def __init__(self, name):
        self.name = name

f = Foo('f')
r = weakref.ref(f)
print(r)
print(r())
print(str(r()))

# This example creates a weak reference to a Foo instance and then
# deletes the Foo instance, making it unreachable.  The weak reference
# is still valid, but attempting to dereference it returns None.

f = Foo('f')
r = weakref.ref(f)
print(r())
del f
print(r())

# This example uses a weak reference to keep a cache of previously
# created objects.  When the cache is full, the least recently used
# object is discarded from the cache.

class Data:
    def __init__(self, value, name):
        self.value
