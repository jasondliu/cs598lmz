import gc, weakref

class MemoryManager:
    """This class keeps track of all objects which the user is allowed to
    modify"""
    def __init__(self):
        self.general_objects = []
        self.special_objects = []

    def register_object(self, obj):
        """Register an object with the memory manager"""
        if obj in self.general_objects:
            return # already registered
        self.general_objects.append(obj)

    def register_special_object(self, obj):
        """Register a special object (like a data source or viewer) with the
        memory manager"""
        if obj in self.special_objects:
            return #already registered
        self.special_objects.append(obj)

    def free_memory(self):
        """Delete all objects which are no longer in use"""
        self.general_objects = [x for x in self.general_objects if x() is not None]
        for obj in self.general_objects:
            if obj() is not None:
                obj().free_memory()
