import gc, weakref

def _finalize_weakref(weak, self):
    del self.__weakrefs[weak]

class Weakrefable(object):
    def __init__(self):
        self.__weakrefs = set()

    def __add_weakref(self, weak):
        self.__weakrefs.add(weak)
        return weak

    def __del__(self):
        for ref in self.__weakrefs:
            if ref() is self:
                ref.finalize()

    def __getstate__(self):
        state = self.__dict__.copy()
        state['__weakrefs'] = None
        return state

    def __setstate__(self, state):
        self.__weakrefs = set()
        self.__dict__ = state

class Bunch(dict):
    """
    A dictionary that provides attribute-style access.
    Taken from
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52308
    """
    def __init__(self, *a,
