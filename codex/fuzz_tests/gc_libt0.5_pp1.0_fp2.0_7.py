import gc, weakref

# This is a list of all the objects that have been created.
all_objects = []

def get_all_objects():
    """Return a list of all objects that have been created."""
    return all_objects

class Object(object):
    """
    An object is any object that can be placed into a room.
    """
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location
        all_objects.append(self)
        self.id = len(all_objects) - 1
        self.ref = weakref.ref(self, self.remove_object)
        
    def remove_object(self, ref):
        """Removes an object from the list of all objects."""
        all_objects.remove(ref)

    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name
        
    def describe(self):
        """Print the description of the object."""
        print
