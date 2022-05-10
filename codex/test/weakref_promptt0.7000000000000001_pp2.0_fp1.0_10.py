import weakref
# Test weakref.ref() and weakref.proxy().

class C(object):
    pass

# Create a strong reference
o = C()

# Create a weak reference
r1 = weakref.ref(o)

# Create a proxy
r2 = weakref.proxy(o)

# Delete the strong reference
del o

# The weak references still work
