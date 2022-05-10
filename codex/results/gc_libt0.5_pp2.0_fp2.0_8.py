import gc, weakref, sys


class ObjectTracker(object):
    """
    This class keeps track of all instances of a class.
    """
    def __init__(self, class_):
        self.class_ = class_
        self.instances = weakref.WeakKeyDictionary()

    def add(self, instance):
        if not isinstance(instance, self.class_):
            raise TypeError("Instance must be of type %s" % self.class_.__name__)
        self.instances[instance] = None

    def remove(self, instance):
        if instance in self.instances:
            del self.instances[instance]

    def __len__(self):
        return len(self.instances)

    def __iter__(self):
        return iter(self.instances.keys())


class ObjectTrackerMeta(type):
    """
    This class is a metaclass that automatically creates an ObjectTracker for
    each class that uses it.
    """
    def __init__(cls, name, bases, dct):
        super(ObjectTrackerMeta,
