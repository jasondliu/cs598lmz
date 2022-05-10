import gc, weakref

class Object(object):
    def __init__(self, name):
        self.name = name
        self.reference_count = 0
        self.weak_references = {}

    def __str__(self):
        return "Object %s, refcount %d" % (self.name, self.reference_count)

    def __repr__(self):
        return "Object %s, refcount %d" % (self.name, self.reference_count)

    def add_weak_reference(self, name, obj):
        self.weak_references[name] = obj

    def remove_weak_reference(self, name):
        del self.weak_references[name]

