import gc, weakref
from . import _weakref


#==============================================================================
# WeakValueDictionary
#==============================================================================
class WeakValueDictionary(object):
    """Mapping class that references values weakly.

    Entries in the dictionary will be discarded when no strong
    reference to the value exists anymore
    """

    def __init__(self, dict=None):
        self.data = {}
        def remove(wr, selfref=weakref.ref(self)):
            self = selfref()
            if self is not None:
                del self.data[wr.key]
        self._remove = remove
        if dict is not None:
            self.update(dict)

    def __getitem__(self, key):
        o = self.data[key]()
        if o is None:
            raise KeyError, key
        else:
            return o

    def __contains__(self, key):
        try:
            o = self.data[key]()
        except KeyError:
            return False
        return o is not None

    has_key = __contains__
