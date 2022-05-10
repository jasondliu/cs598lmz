import weakref
# Test weakref.ref, weakref.proxie

# Create an object with a __weakref__, and use weakref.proxy() to obtain
# a proxy to it.
class Foo:
    pass

foo1 = Foo()
