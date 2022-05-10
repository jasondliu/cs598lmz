import weakref
# Test weakref.ref and weakref.ProxyType

# Test weak references

# Create a weak reference to an object
o = object()
r = weakref.ref(o)
print(r())

# Create a weak reference to an object
o = object()
p = weakref.proxy(o)
print(p)

# Test weak value dictionary

# Create a weak value dictionary
d = weakref.WeakValueDictionary()

# Create a new object
o = object()

# Add the new object to the dictionary
d['obj1'] = o
d['obj2'] = o

# Test if the object is in the dictionary
print('obj1' in d)
print('obj2' in d)

# Remove the object from the dictionary
del o

# Test if the object is in the dictionary
print('obj1' in d)
print('obj2' in d)

# Test the finalizer

# Create a finalizer
def finalize(message):
    print(message)

# Create a new object
o = object()

# Create a weak reference to the object
