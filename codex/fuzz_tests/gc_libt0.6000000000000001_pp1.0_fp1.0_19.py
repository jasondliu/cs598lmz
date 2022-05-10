import gc, weakref

class Object(object):
    def __init__(self, id, name, refs=[]):
        self.id = id
        self.name = name
        self.refs = refs

    # Make an instance printable
    def __repr__(self):
        return 'Object({0})'.format(self.name)


# Create an initial reference to an object
obj = Object('1', 'initial')

# Create a weak reference to it
wref = weakref.ref(obj)

# Enter the object into a dictionary
d = {'primary': obj}

# Print the dictionary
print 'd:', d

# Print the weak reference
print 'wref:', wref

# Print the referent (the referenced object)
print 'wref():', wref()

# Remove the only strong reference to the object
del obj

# Print the weak reference
print 'wref:', wref

# Print the dictionary
print 'd:', d

# Clean up the garbage
gc.collect()

# Print the weak reference
print '
