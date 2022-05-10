import weakref
# Test weakref.ref(getattr(cls, '__weakref__'))

# The new-style class type C.
class C(object):
    pass

# The old-style class type D.
class D(object):
    __metaclass__ = type

class E(object):
    __slots__ = ['foo']

# Create a weak reference to the __weakref__ attribute.
cr = weakref.ref(getattr(C, '__weakref__'))
dr = weakref.ref(getattr(D, '__weakref__'))
er = weakref.ref(getattr(E, '__weakref__'))

# The weak reference should not be dead.
