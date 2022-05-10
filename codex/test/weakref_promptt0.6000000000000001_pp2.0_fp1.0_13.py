import weakref
# Test weakref.ref(obj)

# Create an object, and an instance of it
class Object(object):
    pass

obj = Object()

# Create a weak reference to the object
ref = weakref.ref(obj)

# Print the object's id
