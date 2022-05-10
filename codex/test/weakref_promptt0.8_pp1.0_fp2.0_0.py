import weakref
# Test weakref.ref, weakref.proxy

# Make some objects to work with
a = []
b = []
del a
del b

# Create a weak reference to a list
a = [1, 2, 3]
x = weakref.ref(a)
