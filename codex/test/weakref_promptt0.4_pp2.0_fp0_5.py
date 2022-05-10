import weakref
# Test weakref.ref()

# Create a weak reference to an object

class C:
    pass

o = C()
r = weakref.ref(o)

# Create a strong reference to the same object

s = o

# Remove the strong reference

del o

# Now there are only weak references left

print(r(), s)

# Remove the last reference

del s

# r() now returns None

print(r())

# Create a weak reference to an object

class C:
    pass

o = C()
r = weakref.ref(o)

# Create a strong reference to the same object

s = o

# Remove the strong reference

del o

# Now there are only weak references left

print(r(), s)

# Remove the last reference

del s

# r() now returns None

print(r())

# Create a weak reference to an object

class C:
    pass

o = C()
r = weakref.ref(o)

# Create a strong reference to the same object

