import gc, weakref, sys, os
class Cached(object):
    """A class that keeps a weak reference to its instances.
    """
    def __init__(self):
        self.__cache = weakref.WeakValueDictionary()
    def __repr__(self):
        return "<Cached %s of %d>"%(self.__class__.__name__, len(self.__cache))
    @classmethod
    def get_val(cls, arg):
        try:
            return cls.__cache[arg]
        except KeyError:
            inst = cls(arg)
            cls.__cache[arg] = inst
            return inst

class Card(Cached):
    """A playing card with a value and a suite.
    """
    __cache=weakref.WeakValueDictionary()
    def __init__(self, val, suite):
        self.val = val
        self.suite = suite
    def __repr__(self):
        return "%s%s"%(self.suite, self.val)
    @classmethod
