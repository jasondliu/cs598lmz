import gc, weakref

class Object:
    """
    Instances of this class are used to keep track of all the objects
    that are created, and to make sure that they are deleted before the
    end of the program.
    
    It also allows us to keep track of the references that exist.
    """
    live_objects = {}
    refs_to_objects = {}
    refs_to_objects[0] = set()
    refs_to_objects[1] = set()

    @classmethod
    def get_live_objects(cls):
        return cls.live_objects

    def __init__(self):
        """
        Initialize an object and keep track of it.
        """
        Object.live_objects[self] = True

    def __del__(self):
        """
        Delete a live object and remove it from the list of live objects.
        """
        if self in Object.live_objects:
            del Object.live_objects[self]

    @classmethod
    def print_live_objects(cls):
        """
        Print a list
