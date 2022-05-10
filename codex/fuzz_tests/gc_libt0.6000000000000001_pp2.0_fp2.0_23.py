import gc, weakref, sys, traceback

class ObjectWithID(object):
    """
    A class that has a permanent ID, which is used to identify it.
    """
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return '<%s %d>' % (self.__class__.__name__, self.id)

    def __repr__(self):
        return '<%s %d>' % (self.__class__.__name__, self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return self.id

    def __repr__(self):
        return '<%s %d>' % (self.__class__.__name__, self.id)

class Event(ObjectWithID):
    """
    An event that happens at a specific time.
    """
    def __init__(
