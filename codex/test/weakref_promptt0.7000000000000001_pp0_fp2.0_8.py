import weakref
# Test weakref.ref():

# Create a reference to an object.
obj = object()
r = weakref.ref(obj)
print(obj)

# Look at a weak reference.
print(r)

# Get the object that the weak reference refers to.
print(r())

# Delete the original object.
del obj

# Get the object that the weak reference refers to.
print(r())

# Test weakref.WeakValueDictionary:

# Create an object.
obj = object()

# Create a weak reference to the object.
r = weakref.ref(obj)

# Create a WeakValueDictionary.
wvd = weakref.WeakValueDictionary()

# Add the weak reference to the dictionary.
wvd[1] = r
wvd[2] = r

# Look at the dictionary.
print(wvd)

# Delete the original object.
del obj

# Look at the dictionary.
print(wvd)

# Test weakref.WeakSet:

# Create an object.
obj = object()

# Create a weak reference to
