import weakref
# Test weakref.ref

# Create a class to use as a key
class C:
    pass

# Create a weak reference to a key
r = weakref.ref(C)

# Create a weak reference to an object
o = C()
p = weakref.ref(o)

# Show that the weak references are dead
