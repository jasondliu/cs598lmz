import weakref
# Test weakref.ref

# Create a class that implements __repr__
class C(object):
    pass

c = C()
c.__repr__ = lambda self: "<C instance>"

# Create a weak reference to the instance
r = weakref.ref(c)

# Verify that the weak reference works
