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

    def __del__(self):
        print "Deleting %s" % self.name
        for name, ref in self.weak_references.items():
            print "Removing weak reference %s" % name
            del ref

def create_object(name):
    o = Object(name)
    o.add_weak_reference("ref1", weakref.
